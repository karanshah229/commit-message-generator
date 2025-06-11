import pytest
import os

# Configure pytest to handle async tests
pytest_plugins = ('pytest_asyncio',)

# Add any common fixtures here if needed
@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup and teardown for each test."""
    # Setup
    yield
    # Teardown - ensure we're back on main branch after each test
    os.system('git checkout main')
