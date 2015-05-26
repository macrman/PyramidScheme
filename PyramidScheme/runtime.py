from PyramidScheme.Nodes import *
from PyramidScheme.Types import SchemeProcedure 
import PyramidScheme

import sys

def evaluate(node, env):
    if isinstance(node, Program):
        for expr in node.exprs:
            evaluate(expr, env)
    elif isinstance(node, Num):
        return node.value
    elif isinstance(node, Assign):
        # get the node's var and expr
        key = node.iden.name
        expr = node.expr
        # eval it
        val = evaluate(node.expr, env)
        env[key] = val
        return True
    elif isinstance(node, Call):
        func = evaluate(node.operator, env)
        operands = [evaluate(op,env) for op in node.operands]
        # lambda
        if isinstance(func, SchemeProcedure):
            count = 0
            for parameter in func.parameters.required_args:
                func.env[parameter.name] = operands[count]
                count+=1

            # errors and opt args  
            for expr in func.body:
                result = evaluate(expr, func.env)

            return result
        # user defined funcs...?
        # builtings..
        else:
            result = func(*operands)
            return result
    elif isinstance(node, Id):
        return env[node.name]
    elif isinstance(node, Str):
        return node
    elif isinstance(node, Lambda):
        return SchemeProcedure(node.formals, node.body, env)
    elif isinstance(node, Conditional):
        test = evaluate(node.test, env)
        if(test):
            return evaluate(node.conseq, env)
        elif(node.alt):
            return evaluate(node.alt, env)
    elif isinstance(node, Do):
        # do init & new scope...
        scope_size = len(env.scopes)
        env.enter_scope()
        for spec in node.iter_specs:
            env[spec.iden.name] = evaluate(spec.init, env)
        # now iteration...
        # if test is false...
        test = evaluate(node.test, env)
        while not test:
            # commands...
            for cmd in node.cmds:
                evaluate(cmd, env)
            # step
            for spec in node.iter_specs:
                env[spec.iden.name] = evaluate(spec.step, env)
            # new scope...
            # bind result of step to new scope
            # next iteration
            env.enter_scope()
            test = evaluate(node.test, env)
        # if test is true...
        for expr in node.do_result:
            result = evaluate(expr, env)

        while len(env.scopes) > scope_size:
            env.exit_scope()
        return result
            # eval do result... last one gets returned
    else:
        print(dir(node))
        print(node)
        return "SHIT!!!! YOU FUCKED UP!!!!!"
