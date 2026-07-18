from aeos.startup import Startup

def test_startup():
    assert Startup().initialize() is True
