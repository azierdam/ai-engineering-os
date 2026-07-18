class Application:
    def __init__(self,name): self.name=name
    def with_profile(self,p): self.profile=p; return self
    def with_llm(self,l): self.llm=l; return self
    def build(self): return self
    def run(self): return True
