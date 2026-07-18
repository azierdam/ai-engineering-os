from ai_eos.runtime.service_registry import ServiceRegistry

def test_register():
    r=ServiceRegistry()
    r.register("x",lambda:1)
    assert "x" in r.descriptors()

def test_duplicate():
    r=ServiceRegistry()
    r.register("x",lambda:1)
    try:
        r.register("x",lambda:2)
        assert False
    except ValueError:
        assert True
