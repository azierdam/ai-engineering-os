from ai_eos.runtime.correlation import CorrelationId

def test_correlation():
    assert CorrelationId.new()
