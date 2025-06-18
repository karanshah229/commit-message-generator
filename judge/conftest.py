import pytest
from helpers.llm import run_mcp_server, kill_process

# Configure pytest to handle async tests
pytest_plugins = ('pytest_asyncio',)

# Add any common fixtures here if needed
@pytest.fixture(autouse=True)
def setup_test_environment():
    # Setup
    process = run_mcp_server()
    yield
    # Teardown
    kill_process(process)
