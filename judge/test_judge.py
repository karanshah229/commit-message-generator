import pytest
import json
from judge import run_test_case

# Test cases to run
TEST_CASES = [
    'feat-311',
    'feat-317',
    'fix-359',
    'feat-452'
]

@pytest.mark.asyncio
@pytest.mark.parametrize("branch_name", TEST_CASES)
async def test_commit_message(branch_name):
    """Test that commit messages meet the judging criteria."""
    output = await run_test_case(branch_name)
    raw_output = output['ruling']
    commit_message = output['commit_message']
    # print("RAW OUTPUT FROM JUDGE:", repr(output))
    test_case = json.loads(raw_output)
    
    # Store the results for detailed reporting
    result = {
        'pass': test_case.get('pass', False),
        'improvements': test_case.get('improvements', {}),
        'suggested_commit_message': commit_message
    }
    
    # Assert that the commit message passes all criteria
    assert result['pass'], f"Commit message failed criteria: {result['improvements']}"
    
    # Additional assertions for specific criteria
    criteria = test_case.get('criteria', {})
    assert criteria.get('clear_and_concise', False), "Commit message is not clear and concise"
    assert criteria.get('conventional_commits_format', False), "Commit message does not follow conventional commits format"
    assert criteria.get('relevant_to_changes', False), "Commit message is not relevant to the changes"
    assert criteria.get('consistent_with_previous_commits', False), "Commit message is not consistent with previous commits"
    assert criteria.get('kanban_ticket_details_used_correctly', False), "Kanban ticket details are not used correctly" 
