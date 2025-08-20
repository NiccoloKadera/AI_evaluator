# Libraries
import numpy as np

class GV:
    
    def __init__(self, par):
        
        # Model
        self.E = {} # Dictionary of environmental state
        self.T = 0 # Current time instant
        self.FLAG = True  # Flag for

        self.T_fm = None      
        self.context = ""  
        self.state = {}        

        # Agents
        self.agents_list = []
