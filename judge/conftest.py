import pytest
from helpers.llm import run_mcp_server, kill_process

# Configure pytest to handle async tests
pytest_plugins = ('pytest_asyncio',)

# Add any common fixtures here if needed
@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    # Setup
    print("Setup")
    mcp_server_process = run_mcp_server()
    yield
    print("Teardown")
    # Teardown
    kill_process(mcp_server_process)
