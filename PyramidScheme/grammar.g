from .Nodes import *
%%
parser R7RS:
    ignore: '\\s+'
    token OPAREN: '\('
    token CPAREN: '\)'
    token NUMBER: '[0-9]+'
    token BOOLEAN: '#t|#f|#true|#false'
    token IDENTIFIER: '[-+.><?*/!@%^&=a-zA-Z0-9_]+' 
    token STRING: '"(.*?)"'

    rule identifier:
         IDENTIFIER {{ return Id(IDENTIFIER) }}

    rule expression: 
          identifier {{ return identifier }} 
        | literal {{ return literal }} 
        | OPAREN structured_form CPAREN {{ return structured_form }}

    rule structured_form: 
          assignment {{ return assignment }}
        | procedure_call {{ return procedure_call }}
        | conditional {{ return conditional }}
        | lambda_expression {{ return lambda_expression }}
        | derived_expression {{ return derived_expression }}

    rule lambda_expression:
          "lambda"
          formals 
          body 
          {{ return Lambda(formals, body) }}

    rule formals:
          identifier {{ return Arguments([identifier], []) }}
        | OPAREN 
          paren_formals 
          CPAREN
          {{ return Arguments(paren_formals[0], paren_formals[1]) }}

    rule paren_formals:
        # no args
          {{ args = [] }}
          (identifier {{ args.append(identifier) }})+
          {{ optional_args = None }}
          [optional_args] 
          {{ return [args, optional_args] }}
        | epsilon {{ return ([],[]) }}

    rule optional_args:
          "\." identifier {{ return identifier }}

    rule body:
          # definition
          sequence 
          {{ return sequence }}

    rule sequence:
          {{ seq = [] }}  
          (expression {{ seq.append(expression) }})+ 
          {{ return seq }}

    rule program:
          {{ p = [] }}
          (expression {{ p.append(expression) }})+
          epsilon
          {{ return Program(p) }}

    rule epsilon:
          "" {{ return None }} 

    rule literal:
        self_evaluating {{ return self_evaluating }} 

    rule self_evaluating:
          BOOLEAN 
          {{ boolean = BOOLEAN }}
          {{ return Bool(True if (boolean == "#t" or boolean == "#true") else False) }}
        | NUMBER {{ return Num(int(NUMBER)) }}
        | STRING {{ return Str(STRING[1:-1]) }} 

    rule assignment:
        "set!" identifier expression 
        {{ return Assign(identifier, expression) }}

    rule procedure_call:
        {{ operands = [] }}
        operator 
        (operand {{ operands.append(operand) }})*
        {{ return Call(operator, operands) }}

    rule operand:
        expression {{ return expression }}

    rule operator:
        expression {{ return expression }}

    rule conditional:
        "if" test consequent alternate
        {{ return Conditional(test, consequent, alternate) }}

    rule test:
        expression {{ return expression }}

    rule consequent:
        expression {{ return expression }}

    rule alternate:
          expression {{ return expression }}
        | epsilon {{ return None }}

    rule derived_expression:
          do_expr {{ return do_expr }}

    rule do_expr:
        "do"
        OPAREN 
        {{ iter_specs = [] }}
        (iteration_spec {{iter_specs.append(iteration_spec)}} )* 
        CPAREN
        OPAREN test do_result CPAREN
        {{ cmds = [] }} 
        (expression {{cmds.append(expression) }} )*
        {{ return Do(iter_specs, test, do_result, cmds) }}

    rule iteration_spec:
        {{ step = None }}
        OPAREN identifier init [step] CPAREN
        {{ return IterSpec(identifier, init, step) }}

    rule init:
        expression {{ return expression }}

    rule step:
        expression {{ return expression }}

    rule do_result:
        sequence {{ return sequence }}
        | epsilon {{ return None }}

%%
