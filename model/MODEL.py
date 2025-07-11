from parameters import Par
from global_vars import GV

class Model:
    def __init__(self, parameters: Par = None):
        if parameters is None:
            parameters = Parameters()
        self.parameters = parameters
        self.global_vars = GV(parameters)

    def run(self):