import pytest
from pprint import PrettyPrinter

from PyramidScheme.GeneratedParser import parse
from PyramidScheme.Nodes import *

def test_expr_to_self_eval_bool():
    tree = parse("expression", "#t")
    assert isinstance(tree, Bool)
    assert tree.value == True 

def test_expr_to_id():
    tree = parse("expression", "hello")
    assert isinstance(tree, Id)
    assert tree.name == "hello"

def test_p_expr_to_call():
    tree = parse("expression", "(func 3 4 7 9)")
    assert len(tree.operands) == 4
    first = (tree.operands)[0]
    assert isinstance(first, Num)
    assert first.value == 3

def test_expr_to_assign():
    tree = parse("expression", "(set! x 4)")

def test_super_simple_lambda_def():
    lam_expr = parse("expression", "(lambda y y)")

    args = lam_expr.formals
    required_args = args.required_args
    optional_args = args.optional_args
    body = lam_expr.body

    # testing 
    assert isinstance(lam_expr, Lambda)

    # testing arguments
    assert isinstance(required_args[0], Id)
    assert required_args[0].name == 'y'
    assert len(optional_args) == 0

    # testing body
    assert isinstance(body[0], Id)
    assert body[0].name == 'y'

def test_lambda_with_call():
    lam_expr = parse("expression", "(lambda x (+ x 3) )")
    args = lam_expr.formals
    body = lam_expr.body
    assert isinstance(body[0], Call)

def test_multi_body_empty_arg():
    tree = parse("expression", "(lambda () 4 (+ 3 4) (- 3 4) )") 
    assert len(tree.formals.required_args) == 0
    assert len(tree.formals.optional_args) == 0

    exprs = tree.body
    assert len(exprs) == 3
    assert isinstance(exprs[0], Num)
    assert isinstance(exprs[1], Call)
    assert isinstance(exprs[2], Call)

def test_optional_args():
    tree = parse("expression", "(lambda (x z . y) x)")
    args = tree.formals
    assert len(args.required_args) == 2
    assert args.optional_args.name == 'y'

def test_assign_var_to_lambda():
    tree = parse("expression", "(set! increment (lambda (y) (+ y 1)))")

def test_string():
    tree = parse("expression", '"hello"')
    assert isinstance(tree, Str)

def test_do():
    tree = parse("expression", "(do ((x 0 (+ x 1))) ((> x 5) (display 40)) (display x))")
    print(tree)

    assert isinstance(1, Do)
