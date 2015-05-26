from PyramidScheme.BaseLibrary import builtins

def test_math():
    assert callable(builtins['+'])
    assert builtins['+'](1,2,3) == 6
    assert builtins['-'](8,4,1) == 3
    assert builtins['*'](1,2,3) == 6
    assert builtins['/'](12,4,3) == 1
    assert builtins['zero?'](0)
    assert builtins['sub1'](2) == 1

def test_control_flow():
    assert builtins['if'](0,1,2) == 2
    assert builtins['if'](1,1,2) == 1
    assert builtins['if'](0,1) is None 
    assert builtins['if'](1,1) == 1

def test_string():
    from PyramidScheme.Nodes import Str
    string1 = Str('hello')
    assert builtins['string?'](string1)
    # testing str copy
    string2 = builtins['string-copy'](string1)
    assert id(string1) != id(string2)
    # testing substring..
    assert builtins['substring'](string1, 1).s == 'ello'
    assert builtins['string-length'](string1) == 5
    assert builtins['string<?'](string1, string2) == False
    assert builtins['string>?'](string1, string2) == False
    string3 = Str('ello')
    assert builtins['string>=?'](string2, string3)


