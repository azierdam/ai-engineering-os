from aeos.runtime import Runtime

def test_runtime_start():
    assert Runtime().start() == "AEOS runtime started"
