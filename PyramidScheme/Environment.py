from PyramidScheme.BaseLibrary import builtins

class BaseEnv():
    """
    Enviroments are a stack of scopes. Key lookups search from the end of the
    list to the bottom, the bottom being the builtins
    """
    def __init__(self, *args):
        """
        uhh yeah....
        """
        self.scopes = [builtins]
        for arg in args:
            # check for dicts...?
            self.scopes.append(args)
        self.scopes.append({})
        
    def __getitem__(self, key):
        for scope in reversed(self.scopes):
            if key in scope:
                return scope[key]
        # raise an error
        raise KeyError

    def __setitem__(self, key, value):
        self.scopes[-1][key] = value

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop(-1)
    
    def __str__(self):
        return str(self.scopes)
