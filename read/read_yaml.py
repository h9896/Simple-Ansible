import yaml
import os

class ReadYaml:
    def __init__(self, path):
        self.path = path
        self.data = None
    def read(self) -> bool:
        if os.path.isfile(self.path):
            with open(self.path, 'r') as stream:
                self.data = yaml.load(stream, Loader = yaml.FullLoader)
        if self.data:
            return True
        else:
            return False