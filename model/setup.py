# Libraries
import random
import numpy as np

# Model
from parameters import Par
from global_vars import GV
from agent import Agent


def setup_seed(par: Par):
    if par.seed is not None:
        random.seed(par.seed)
        np.random.seed(par.seed)

def setup_agents(par: Par, gv: GV):
    for i in range(par.n):  # esempio con 10 agenti
        new_agent = Agent(
            id=i,
            ag_type="standard",
            client_llm=None  # oppure un oggetto se previsto
        )
        gv.agents_list.append(new_agent)

def setup_pipeline(par: Par, gv: GV):
    setup_seed(par)
    setup_agents(par, gv)
    

