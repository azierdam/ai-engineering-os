class CapabilityDispatcher:
    def dispatch(self, agent, capability, *args, **kwargs):
        fn=getattr(agent, capability)
        return fn(*args, **kwargs)
