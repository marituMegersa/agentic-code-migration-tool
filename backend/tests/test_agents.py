def test_agent_orchestrator():
    prompt = "Test execution query for agentic-code-migration-tool"
    assert len(prompt) > 0
    assert "Test" in prompt
