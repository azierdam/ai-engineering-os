from aeos.healthcheck import HealthCheck

def test_healthcheck():
    assert HealthCheck().initialize() is True
