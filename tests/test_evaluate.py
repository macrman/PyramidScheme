import pytest
from PyramidScheme.runtime import evaluate
from PyramidScheme.GeneratedParser import parse
from PyramidScheme.Environment import BaseEnv
from PyramidScheme.Nodes import *
from PyramidScheme.Types import SchemeProcedure

def test_evaluate_add():
    env = BaseEnv()
    tree = parse("expression", "(+ 3 4)")
    assert evaluate(tree, env) == 7
    nested_expr = parse("expression", "(* (- 6 2) 2)")
    assert evaluate(nested_expr, env) == 8

def test_eval_conditional():
    env = BaseEnv()
    tree = parse(
        "expression",
        "(if (- 4 2) 9 2)"
    )
    assert evaluate(tree, env) == 9
    assert evaluate(parse("expression", "(if (zero? 1) 0 1)"), env) == 1
    assert evaluate(parse("expression", "(if (zero? 0) 0 1)"), env) == 0

def test_assignment():
    env = BaseEnv()
    tree = parse("expression", "(set! x 4)")
    evaluate(tree, env)
    assert env["x"] == 4

    othertree = parse("expression", "(set! y (+ 3 4))")
    evaluate(othertree, env)
    assert env["y"] == 7

def test_sequence_of_exprs():
    env = BaseEnv()
    trees = parse("program", "(set! x 4)(set! y (+ x 3))")
    assert len(trees.exprs) == 2
    evaluate(trees, env)
    assert env["y"] == 7

def test_lambda_has_own_scopes_and_can_eval():
    env = BaseEnv()
    init_num_of_scopes = len(env.scopes)
    tree = parse("expression", "(set! increment (lambda (me) (set! z 1)(+ me z)))")
    evaluate(tree, env)
    with pytest.raises(KeyError):
        env["z"]
    assert isinstance(env["increment"], SchemeProcedure)
    nextproc = parse("expression", "(increment 2)")
    # now lets try a func call....
    assert evaluate(nextproc, env) == 3

    # make sure our localaly defined ids went out of scope
    with pytest.raises(KeyError):
        env["z"]
        env["me"]

    # make sure we have the correct number of scopes as we did initially
    assert len(env.scopes) == init_num_of_scopes

def test_im_fucked():
    env = BaseEnv()
    demo = parse("expression", "(lambda (x) (+ x 2)(+ 2 3))")
    expr =  """
        (
            (
                (lambda (x) (x x)) 
                (lambda (factgen) 
                    (
                        lambda 
                        (n)
                        (if (zero? n) 1 (* n ( (factgen factgen) (sub1 n) )))
                    )
                )
            ) 5
        )
    """
    #expr =
    """
    (set! dectozero 
    )
    """
    tree = parse("expression", expr) 

    assert evaluate(tree, env) == 120

def test_do_loop():
    env = BaseEnv()
    og_scope_size = len(env.scopes)
    tree = parse("expression", "(do ((x 0 (+ x 1))) ((> x 5) (display 40)) (display x))")
    evaluate(tree, env)
    assert og_scope_size == len(env.scopes)

