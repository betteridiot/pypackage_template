# Python Package Template

A comprehensive Python package template with integrated CI/CD, testing, documentation, and development tools.

## Features

- Source package layout with type hints
- Comprehensive testing suite (unit, integration, e2e)
- Automated documentation generation
- Code quality enforcement
- Version management
- CI/CD pipeline integration
- Development automation

## Directory Structure

```
pypackage_template/
├── src/                            # Source code directory
│   └── pypackage_template/         # Main package
├── tests/                          # Test directory
│   ├── conftest.py                 # Shared pytest fixtures
│   ├── unit/                       # Unit tests
│   ├── integration/                # Integration tests
│   └── e2e/                        # End-to-end tests
├── docs/                           # Documentation
│   └── source/                     # Documentation source
├── scripts/                        # Utility scripts
├── .github/                        # GitHub specific files
│   └── workflows/                  # GitHub Actions
└── [Configuration Files]           # Various tool configs
```

## Development Tools

### Package Management
- **Poetry**: Dependency management and packaging
  - Installation: `pip install poetry`
  - Initialize: `poetry install --with dev,docs,test,build`
  - Virtual Environment: `poetry shell`

### Testing
- **pytest**: Test framework with plugins
  - Run tests: `poetry run pytest`
  - Coverage: `poetry run pytest --cov`
  - Parallel testing: `poetry run pytest -n auto`

### Documentation
- **Sphinx**: Documentation generator
  - Build docs: `cd docs && poetry run make html`
  - Live preview: `cd docs && poetry run make livehtml`

### Code Quality
- **black**: Code formatting
- **flake8**: Code linting
- **mypy**: Type checking
- **bandit**: Security checks
- **pre-commit**: Git hooks
  - Install hooks: `pre-commit install --install-hooks`

### Version Management
- **poetry-dynamic-versioning**: Automatic versioning
  - Based on git tags
  - Automatically updates `__version__`

## Required Customization

### Files to Modify
1. `pyproject.toml`:
   - `name`
   - `description`
   - `authors`
   - `repository`
   - `documentation`
   - `Bug Tracker` URL

2. `docs/source/conf.py`:
   - `project`
   - `copyright`
   - `author`

3. `.github/workflows/*.yml`:
   - Repository secrets
   - Environment variables

4. `README.md`:
   - Project description
   - Installation instructions
   - Usage examples

### Quick Start
Use the provided customization script:
```bash
python scripts/customize_template.py \
    --name "your-package-name" \
    --author "Your Name" \
    --email "your.email@example.com" \
    --description "Your package description" \
    --github-username "your-github-username"
```

## Development Commands

### Testing
```bash
poetry run pytest                    # Run all tests
poetry run pytest tests/unit         # Run unit tests
poetry run pytest -v -m "not slow"   # Skip slow tests
poetry run pytest --cov              # Run with coverage
```

### Documentation
```bash
cd docs
poetry run make html                 # Build HTML docs
poetry run make doctest              # Test code examples
```

### Code Quality
```bash
poetry run black .                   # Format code
poetry run flake8                    # Lint code
poetry run mypy src                  # Type check
poetry run bandit -r src             # Security check
```

### Building and Publishing
```bash
poetry build                         # Build package
poetry publish                       # Publish to PyPI
```

## Automated Features

- **Version Management**: Handled by poetry-dynamic-versioning
- **Documentation**: Auto-generated from docstrings
- **Test Coverage**: Auto-generated reports
- **CI/CD**: Automated by GitHub Actions
- **Dependency Updates**: Managed by Poetry

## Configuration Files

- `pyproject.toml`: Main project configuration
- `tox.ini`: Multi-environment testing
- `.pre-commit-config.yaml`: Git hooks
- `.readthedocs.yaml`: Documentation building
- `MANIFEST.in`: Package file inclusion
- `.gitignore`: Git exclusions

## Getting Started

1. Clone the template
2. Run the customization script
3. Initialize git repository
4. Create initial version tag
5. Install development dependencies
6. Setup pre-commit hooks
7. Start developing!

## Maintenance

### Manual Updates Required
- Package version tags
- Documentation content
- Test cases
- Source code
- Dependency versions (as needed)

### Automated Updates
- Package version (via git tags)
- Test coverage reports
- Documentation builds
- Code formatting
- Dependency resolution

For detailed information about each tool and configuration, refer to the documentation in `docs/`.

I'll add these sections to the existing README.md:

## GitHub Setup

### Repository Configuration
1. Create a new repository on GitHub
2. Go to Settings → Actions → General
   - Set "Actions permissions" to "Allow all actions and reusable workflows"
   - Enable "Allow GitHub Actions to create and approve pull requests"

### Branch Protection
1. Go to Settings → Branches → Branch protection rules
2. Click "Add rule" and configure:
   - Branch name pattern: `main`
   - Check "Require a pull request before merging"
   - Check "Require status checks to pass before merging"
   - Check "Require branches to be up to date before merging"
   - Select status checks: `tests`, `docs`, `lint`
   - Check "Include administrators"
   - Check "Allow force pushes" (optional for maintainers)

## Package Distribution and Services

### PyPI Setup
PyPI (Python Package Index) is the official repository for Python packages. To publish your package:
1. Create account at https://pypi.org/account/register/
2. Generate API token:
   - Go to Account settings → API tokens
   - Create a new token with "Upload to PyPI" scope
   - Save token for GitHub secrets configuration

### Codecov Setup
Codecov provides code coverage reporting and visualization:
1. Sign up at https://codecov.io using GitHub
2. Add your repository to Codecov
3. Get your repository token:
   - Go to Repository Settings → General
   - Copy the Repository Upload Token
   - Save token for GitHub secrets configuration

### ReadTheDocs Setup
ReadTheDocs hosts and automatically builds documentation:
1. Sign up at https://readthedocs.org using GitHub
2. Import your repository
3. Generate API token:
   - Go to Account Settings → API Tokens
   - Create new token with "Read the Docs" scope
   - Save token for GitHub secrets configuration

### GitHub Secrets Configuration
1. Go to Settings → Secrets and variables → Actions
2. Add required secrets:
   - `PYPI_TOKEN`: For package publishing
   - `CODECOV_TOKEN`: For coverage reporting
   - `READTHEDOCS_TOKEN`: For documentation builds

### Conda-forge Setup
1. Fork conda-forge/staged-recipes
2. Create new recipe in `recipes/pypackage_template/meta.yaml`:
```yaml
{% set name = "pypackage_template" %}
{% set version = "0.1.0" %}

package:
  name: {{ name|lower }}
  version: {{ version }}

source:
  url: https://pypi.io/packages/source/{{ name[0] }}/{{ name }}/{{ name }}-{{ version }}.tar.gz
  sha256: [SHA256 hash of your package]

build:
  number: 0
  noarch: python
  script: {{ PYTHON }} -m pip install . -vv

requirements:
  host:
    - python >=3.8
    - pip
  run:
    - python >=3.8

test:
  imports:
    - pypackage_template
  commands:
    - pip check
  requires:
    - pip

about:
  home: https://github.com/betteridiot/pypackage_template
  license: MIT
  license_file: LICENSE
  summary: Your package description
```

3. Submit pull request to conda-forge/staged-recipes

## Automated CI/CD

### Automated Quality Checks
The CI pipeline automatically runs these tools:
- **black**: Code formatter that enforces consistent style
- **flake8**: Linter that checks for style and syntax errors
- **mypy**: Static type checker for Python type annotations
- **bandit**: Security vulnerability scanner
- **pytest**: Testing framework for running test suite

Configure in `.github/workflows/ci.yml`:
```yaml
    - name: Run quality checks
      run: |
        poetry run black . --check
        poetry run flake8 .
        poetry run mypy src/
        poetry run bandit -r src/
```

### Automated Publishing
Package publishing is triggered on release:
1. Create new tag: `git tag v0.1.0`
2. Push tag: `git push --tags`
3. Create GitHub release
4. CI automatically:
   - Builds package
   - Runs tests
   - Updates documentation
   - Publishes to PyPI
   - Updates conda-forge (via bot)

### Version Management
Version updates are handled by poetry-dynamic-versioning:
1. Create new tag for version
2. Push tag to trigger release workflow
3. CI automatically:
   - Updates package version
   - Updates changelog
   - Creates release
   - Publishes package

### Documentation Updates
Documentation is automatically:
1. Built on every push to main
2. Published to ReadTheDocs
3. Updated for new releases
4. Tested for code examples

Configure in `.github/workflows/docs.yml` and `.readthedocs.yaml`

These automated processes ensure:
- Consistent code quality
- Reliable testing
- Up-to-date documentation
- Proper version management
- Automated distribution

For detailed workflow configurations, see the `.github/workflows/` directory.

