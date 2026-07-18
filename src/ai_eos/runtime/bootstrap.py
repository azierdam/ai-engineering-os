from .composition_root import CompositionRoot
from .service_registry import ServiceRegistry
from .container import Container
def create_runtime():
    root=CompositionRoot()
    registry=ServiceRegistry()
    return {"root":root,"registry":registry,"container":Container(registry)}
