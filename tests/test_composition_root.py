from ai_eos.runtime.composition_root import CompositionRoot

def test_build_empty():
    assert CompositionRoot().build()=={}
