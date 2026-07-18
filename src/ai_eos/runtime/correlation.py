from uuid import uuid4
class CorrelationId:
    @staticmethod
    def new()->str:
        return str(uuid4())
