from copy import deepcopy
class SchemeProcedure():

    def __init__(self, parameters, body, env):
        self.parameters = parameters
        self.body = body
        self.env = deepcopy(env)
