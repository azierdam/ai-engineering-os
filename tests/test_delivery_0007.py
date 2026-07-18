from aeos.runtime_container import RuntimeContainer

def test_runtime_container():
    assert RuntimeContainer().initialize() is True
