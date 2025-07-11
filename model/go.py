# Libraries

# Model
from parameters import Par
from global_vars import GV

def go(par: Par, gv: GV):
    gv.T += 1

    for ag in gv.agents_list:
        # Esempio di aggiornamento dell’agente
        ag.Action_Dict["azione_corrente"] = "esempio"
        ag.State_Dict_Ag["ultimo_turno"] = gv.T

    if gv.T >= 100:
        gv.FLAG = False
