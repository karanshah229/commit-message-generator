import pytest
import json
import re
from judge import run_test_case

TEST_CASES = [
    'feat-311',
    'feat-317',
    'fix-359',
    'feat-452'
]

def extract_json_from_response(response):
    match = re.search(r'```json\n(.*?)\n```', response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return response

@pytest.mark.asyncio
@pytest.mark.parametrize("branch_name", TEST_CASES)
async def test_commit_message(branch_name, setup_test_environment):
    """Test that commit messages meet the judging criteria."""
    output = await run_test_case(branch_name)
    raw_output = output['ruling']
    commit_message = output['commit_message']
    json_output = extract_json_from_response(raw_output)
    test_case = json.loads(json_output)
    
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
