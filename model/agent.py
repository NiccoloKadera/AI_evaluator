class Agent:
    def __init__(self, id, ag_type, client_llm=None):
        self.id = id
        # Agent state dictionary with 'state1' key and related fields
        self.states_dict = {
            'state1': {
                'meaning': 'state description',
                'allowed_value': [],           # list or set of allowed values
                'initial_value': None,
                'current_value': None,
                'dynamics': None,              # function or dynamic description
                'time_series_values': []       # time series or list of values over time
            }
        }
        # Dictionary of possible actions with 'action1' key and related fields
        self.actions_dict = {
            'action1': {
                'meaning': 'action description',
                'allowed_values': [],          # list or set of allowed values
                'type': None,                  # 'AI' or 'Not AI'
                'action': None                 # function or action description
            }
        }
        self.client_llm = client_llm # LLM Client associated with the agent
        self.ag_type = ag_type # Agent type
