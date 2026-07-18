import os
class RuntimeEnvironment:
    def get(self,key,default=None):
        return os.getenv(key,default)
