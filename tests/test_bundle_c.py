from ai_eos.runtime.mock_llm import MockLLMProvider
def test_mock():
    assert MockLLMProvider().generate("hi")=="mock:hi"
