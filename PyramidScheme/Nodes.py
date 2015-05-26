class Node:
    _fields = []

    def __init__(self, *args):
        for key, value in zip(self._fields, args):
            setattr(self, key, value)
    def __repl__(self):
        return self.__str__()

# literals...
class Bool(Node):
    _fields = ["value"]
    
    def __str__(self):
        string = "Boolean=" + str(self.value) 
        return string 

class Num(Node):
    _fields = ["value"]

    def __str__(self):
        string = "Number=" + str(self.value)
        return string

class Str(Node):
    _fields = ["s"]

    def __str__(self):
        string = "String=" + str(self.s)
        return string

# ids..
class Id(Node):
    _fields = ["name"]

    def __str__(self):
        return "Id=" + str(self.name)

# expressions
class Expr(Node):
    _fields = ["body"]
    
    def __str__(self):
        return "Expression(" + str(self.body) + ")"

class Assign(Node):
    _fields = ["iden", "expr"]
        
    def __str__(self):
        return "Assign(" + str(self.iden) + ", " + str(self.expr) + ")"

class Call(Node):
    _fields = ["operator", "operands"]
        
    def __str__(self):
        operands = ""
        for operand in self.operands:
            operands += (str(operand) + ', ')
        return "Call(" + str(self.operator) + ", [" + operands + "])"

class Lambda(Node):
    _fields = ["formals", "body"]

    def __str__(self):
        body = ""
        for exp in self.body:
            body += (str(exp) + ', ')
        return "Lambda(formals = " + str(self.formals) + ", body=" + body + ")"

class Arguments(Node):
    _fields = ["required_args", "optional_args"]

    def __str__(self):
        r_args = ''
        for arg in self.required_args:
            r_args += (str(arg) + ", ")
        o_args = ''
        if self.optional_args:
            for arg in self.optional_args:
                o_args += (str(arg) + ", ")
        return "r_args=[" + r_args  + "], o_args=[" + o_args + "]"

class Program(Node):
    _fields = ["exprs"]

    def __str__(self):
        return "Program(" + str(self.exprs) + ")"

class Conditional(Node):
    _fields = ["test", "conseq", "alt"]

    def __str__(self):
        test = str(self.test)
        then = str(self.conseq)
        el = str(self.alt)
        return "Conditional(if=" + test + ", then=" + then + ", else=" + el + ")"

class Do(Node):
    _fields = ["iter_specs", "test", "do_result", "cmds"]

    def __str__(self):
        specs =""
        for spec in self.iter_specs:
            specs += (str(spec) + ", ")
        test = str(self.test)
        do_result = str(self.do_result)
        return "Do((" + specs + "), " + test + do_result + str(self.cmds) + ")"


class IterSpec(Node):
    _fields = ["iden", "init", "step"]

    def __str__(self):
        return "IterSpec(" + str(self.iden) + ", " + str(self.init) + ", " + str(self.step) + ")"
