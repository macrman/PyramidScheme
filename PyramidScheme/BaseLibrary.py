from copy import deepcopy
from operator import add, sub, mul, truediv
from .Nodes import *

# SCHEME BUILTINS
def conditional(condition, consequent, alternate=None):
    if(condition):
        return consequent
    else:
        return alternate

def ps_set(identifier, expr):
    return True

def ps_display(*args):
    print(*args)

# MATH STUFF
def ps_add(*args):
    args = list(args)
    result = args.pop(0)
    for arg in args:
        result += arg
    return result

def ps_sub(*args):
    args = list(args)
    result = args.pop(0)
    for arg in args:
        result = result - arg 
    return result

def ps_mul(*args):
    args = list(args)
    result = args.pop(0)
    for arg in args:
        result = result * arg
    return result

def ps_div(*args):
    args = list(args)
    result = args.pop(0)
    for arg in args:
        result = result / arg
    return result

def ps_greater(a,b):
    if a > b:
        return True
    return False

def ps_less(a,b):
    if a < b:
        return True
    return False

def ps_greater_e(a,b):
    if a >= b:
        return True
    return False

def ps_less_e(a,b):
    if a <= b:
        return True
    return False

def ps_equal(a,b):
    return a == b

def ps_sub1(arg):
    return arg - 1

def ps_zero_q(arg):
    if arg == 0:
        return True
    else:
        return False

# STRING STUFF
def ps_string_q(s):
    if isinstance(s, Str):
        return True
    return False

def ps_string_to_list(s):
    pass

def ps_string_copy(s):
    new_s = deepcopy(s)
    return new_s

def ps_substring(s, start, end=None):
    if(end):
        new_s = s.s[start:end]
    else:
        new_s = s.s[start:]
    return Str(new_s)


def ps_string_length(s):
    return len(s.s)

def ps_string_less_e_q(s1, s2):
    return s1.s <= s2.s
 
def ps_string_great_e_q(s1, s2):
    return s1.s >= s2.s

def ps_string_e_q(s1, s2):
    return s1.s == s2.s

def ps_string_less_q(s1, s2):
    return s1.s < s2.s

def ps_string_great_q(s1, s2):
    return s1.s > s2.s


builtins = {
    '+': ps_add,
    '-': ps_sub,
    '*': ps_mul,
    '/': ps_div,
    '<': ps_less,
    '>': ps_greater,
    '<=': ps_less_e,
    '>=': ps_greater_e,
    '=': ps_equal,
    'if': conditional,
    'sub1': ps_sub1,
    'zero?': ps_zero_q,
    'display': ps_display,
    'string?': ps_string_q,
    'string->list': ps_string_to_list,
    'string-copy': ps_string_copy,
    'substring': ps_substring,
    'string-length': ps_string_length,
    'string<=?': ps_string_less_e_q,
    'string>=?': ps_string_great_e_q,
    'string=?': ps_string_e_q,
    'string<?': ps_string_less_q,
    'string>?': ps_string_great_q,
}
