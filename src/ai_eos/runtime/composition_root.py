"""Composition Root."""
from typing import Callable, Any

class CompositionRoot:
    def __init__(self)->None:
        self._services:dict[str,Callable[[],Any]]={}
    def register(self,name:str,factory:Callable[[],Any])->None:
        self._services[name]=factory
    def build(self)->dict[str,Any]:
        return {k:v() for k,v in self._services.items()}
