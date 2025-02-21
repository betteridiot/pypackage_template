"""
Global pytest configuration and fixtures.

This module provides shared fixtures and configurations for all test types:
- Unit tests
- Integration tests
- End-to-end tests
"""

import os
import pathlib
import pytest
from typing import Generator, Any, Dict


@pytest.fixture(scope="session")
def test_dir() -> pathlib.Path:
    """Return the directory containing the test files."""
    return pathlib.Path(__file__).parent


@pytest.fixture(scope="session")
def data_dir(test_dir: pathlib.Path) -> pathlib.Path:
    """Return the directory containing test data files."""
    data_path = test_dir / "data"
    if not data_path.exists():
        data_path.mkdir(parents=True)
    return data_path


@pytest.fixture(scope="session")
def temp_dir(tmp_path_factory: pytest.TempPathFactory) -> Generator[pathlib.Path, None, None]:
    """Create and return a temporary directory for test files."""
    temp_path = tmp_path_factory.mktemp("temp")
    yield temp_path


@pytest.fixture(scope="function")
def clean_environment() -> Generator[Dict[str, str], None, None]:
    """Provide a clean environment for tests that modify environment variables."""
    original_environ = dict(os.environ)
    yield os.environ
    os.environ.clear()
    os.environ.update(original_environ)


@pytest.fixture(scope="session")
def sample_data() -> Dict[str, Any]:
    """Provide sample data for tests."""
    return {
        "string": "test",
        "integer": 42,
        "float": 3.14,
        "list": [1, 2, 3],
        "dict": {"key": "value"},
    }


@pytest.fixture(autouse=True)
def _configure_logging(caplog: pytest.LogCaptureFixture) -> None:
    """Configure logging for all tests."""
    caplog.set_level("DEBUG")


def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "e2e: marks tests as end-to-end tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Modify test items in-place to add markers based on path."""
    for item in items:
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "e2e" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)


@pytest.fixture(scope="session")
def mock_config() -> Dict[str, Any]:
    """Provide mock configuration for tests."""
    return {
        "api_key": "test_key",
        "base_url": "http://test.com",
        "timeout": 30,
        "retries": 3,
    }


@pytest.fixture(scope="function")
def cleanup_files(temp_dir: pathlib.Path) -> Generator[None, None, None]:
    """Clean up any files created during tests."""
    yield
    for item in temp_dir.iterdir():
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            for subitem in item.iterdir():
                subitem.unlink()
            item.rmdir()
