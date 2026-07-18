from .llm_adapter import LLMAdapter
class MockLLMProvider(LLMAdapter):
    def generate(self,prompt:str)->str:
        return f"mock:{prompt}"
