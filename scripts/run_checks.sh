#!/usr/bin/env bash
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print status messages
print_status() {
    echo -e "${BLUE}[*] $1${NC}"
}

# Function to print success messages
print_success() {
    echo -e "${GREEN}[+] $1${NC}"
}

# Function to print error messages
print_error() {
    echo -e "${RED}[-] $1${NC}"
}

# Function to run a command and check its status
run_check() {
    print_status "Running $1..."
    if eval "$2"; then
        print_success "$1 passed"
    else
        print_error "$1 failed"
        exit 1
    fi
}

# Ensure we're in the poetry environment
if [ -z "$POETRY_ACTIVE" ]; then
    print_status "Activating poetry environment..."
    eval "$(poetry env use python)"
fi

# Run all checks
run_check "black" "poetry run black --check ."
run_check "isort" "poetry run isort --check-only ."
run_check "flake8" "poetry run flake8 ."
run_check "mypy" "poetry run mypy src/"
run_check "bandit" "poetry run bandit -c pyproject.toml -r src/"
run_check "pydocstyle" "poetry run pydocstyle --convention=google src/"
run_check "pytest" "poetry run pytest --cov --cov-report=term-missing"

# Build documentation
print_status "Building documentation..."
cd docs && poetry run make html
cd ..

# Check if running in CI environment
if [ -z "$CI" ]; then
    # Run additional local checks
    run_check "pre-commit" "poetry run pre-commit run --all-files"
    
    print_status "Checking for uncommitted changes..."
    if ! git diff --quiet HEAD; then
        print_error "There are uncommitted changes"
        git status --short
        exit 1
    fi
fi

print_success "All checks passed successfully!"
