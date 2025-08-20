# Libraries

# Model
from parameters import Par
from global_vars import GV

def go(par: Par, gv: GV, input_1=None, input_2=''):
    gv.T += 1

    # Predefined variables
    agents_list = gv.agents_list

    # Executing actions
    
    if input_1 == None:
        eval(input_2)
    else:
        for el in eval(input_1):
            eval(input_2)
            pass

    # Updating gv.variables
    gv.agents_list = agents_list

    if gv.T >= 100:
        gv.FLAG = False
