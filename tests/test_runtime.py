from ai_eos.runtime.health import health_check
from ai_eos.runtime.application import Application

def test_health(): assert health_check()['status']=='ok'
def test_app(): assert Application('pfl').build().run()
