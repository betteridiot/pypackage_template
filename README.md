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
│       ├── __init__.py             # Package metadata
│       ├── py.typed                # Type hint marker
│       ├── core.py                 # Core functionality
│       ├── analysis.py             # Analysis modules
│       └── utils.py                # Utility functions
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
poetry run pytest --cov             # Run with coverage
```

### Documentation
```bash
cd docs
poetry run make html                # Build HTML docs
poetry run make doctest            # Test code examples
```

### Code Quality
```bash
poetry run black .                  # Format code
poetry run flake8                  # Lint code
poetry run mypy src                # Type check
poetry run bandit -r src           # Security check
```

### Building and Publishing
```bash
poetry build                       # Build package
poetry publish                     # Publish to PyPI
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
