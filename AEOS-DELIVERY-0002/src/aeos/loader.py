from .registry import AgentRegistry

class AgentLoader:
    def __init__(self, registry: AgentRegistry):
        self.registry=registry
    def load(self,name,factory):
        self.registry.register(name,factory())
