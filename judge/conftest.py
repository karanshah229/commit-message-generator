import pytest
from helpers.llm import run_mcp_server, kill_process
from test_judge import TEST_CASES
from helpers.git import delete_local_branch, delete_remote_branch

# Configure pytest to handle async tests
pytest_plugins = ('pytest_asyncio',)

# Add any common fixtures here if needed
@pytest.fixture(scope="session")
def setup_test_environment():
    # Setup
    print("Setup")
    mcp_server_process = run_mcp_server()
    yield
    print("Teardown")
    # Teardown
    kill_process(mcp_server_process)

    # Clean up test branches after each test
    print("Cleanup branches---------------------------")
    for branch_name in TEST_CASES:
        delete_local_branch(branch_name, force=True)
        delete_remote_branch(branch_name, force=True)
