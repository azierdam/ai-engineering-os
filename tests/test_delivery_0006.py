from aeos.runtime_monitor import RuntimeMonitor

def test_runtime_monitor():
    assert RuntimeMonitor().initialize() is True
