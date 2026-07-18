from .service_registry import ServiceRegistry
class Container:
    def __init__(self, registry: ServiceRegistry):
        self._r=registry; self._singletons={}
    def resolve(self,name:str):
        d=self._r.descriptors()[name]
        if d.singleton:
            if name not in self._singletons:
                self._singletons[name]=d.factory()
            return self._singletons[name]
        return d.factory()
