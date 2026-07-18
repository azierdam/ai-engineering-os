from aeos.workflow import WorkflowExecutor

def test_run():
    assert WorkflowExecutor().run([lambda:1,lambda:2])==[1,2]
