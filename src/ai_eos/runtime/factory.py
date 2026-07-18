from .bootstrap import create_runtime
def create(profile:str="development"):
    return create_runtime()
