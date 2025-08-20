# Libraries

# Model
from parameters import Par
from global_vars import GV

def go(par: Par, gv: GV):
    gv.T += 1

    for ag in gv.agents_list:
        # ag.actions_dict["azione_corrente"] = "esempio"
        # ag.states_dict["ultimo_turno"] = gv.T
        pass

    if gv.T >= 100:
        gv.FLAG = False
