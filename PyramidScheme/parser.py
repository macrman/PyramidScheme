from .Nodes import *
from .GeneratedParser import R7RS


def parse(rule, text):
    P = Scheme(SchemeScanner(text))
    return runtime.wrap_error_reporter(P, rule)
