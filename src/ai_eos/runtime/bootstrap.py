from .composition_root import CompositionRoot

def create_runtime()->dict[str,object]:
    root=CompositionRoot()
    return root.build()
