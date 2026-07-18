from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class ServiceDescriptor:
    factory: Callable[[], Any]
    singleton: bool = True

class ServiceRegistry:
    def __init__(self):
        self._services: dict[str, ServiceDescriptor] = {}

    def register(self,name:str,factory:Callable[[],Any],singleton:bool=True)->None:
        if name in self._services:
            raise ValueError(f"Service '{name}' already registered")
        self._services[name]=ServiceDescriptor(factory,singleton)

    def descriptors(self)->dict[str,ServiceDescriptor]:
        return dict(self._services)
