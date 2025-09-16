# Libraries

# Model
from parameters import Par
from global_vars import GV
from ABML_translation import ABML_translation

def go(par: Par, gv: GV):
    gv.T += 1

    # Initializing translator
    translator = ABML_translation()


    # Defining local variables
    local_vars = {
        'agents_list': gv.agents_list,
        't': gv.T,
        'par': par,
        'gv': gv,
    }

    # Executing actions    
    
    if par.go_set == None:        
        translated_code = translator.translate_to_py(par.go_el)
        exec(translated_code, globals(), local_vars)
    else:
        
        for_elements = eval(par.go_set, globals(), local_vars)
        for el in for_elements:
            
            local_vars['el'] = el
            translated_code = translator.translate_to_py(par.go_el)
            exec(translated_code, globals(), local_vars)
            pass

    # Updating gv.variables
    gv.agents_list = local_vars['agents_list']

    if gv.T >= 100:
        gv.FLAG = False
