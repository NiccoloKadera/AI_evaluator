# Model
from parameters import Par
from global_vars import GV
from setup import setup_pipeline
from go import go
from output import ABML_Mermaid

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
    
    def mermaid_go_el(self):
        abml_m = ABML_Mermaid()
        mermaid_code = abml_m.convert_to_mermaid(self.par.go_el)
        return mermaid_code