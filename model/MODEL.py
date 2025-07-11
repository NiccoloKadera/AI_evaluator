# Model
from parameters import Par
from global_vars import GV
from setup import setup_pipeline
from go import go

class Model:
    def __init__(self, par: Par = None):
        if par is None:
            par = Par()

        self.par = par
        self.gv = GV(par)

        setup_pipeline(self.par, self.gv)

    def run(self):
        while self.gv.FLAG:
            go(self.par, self.gv)