import pytest
def test_file1_method1():
    x=6
    y=6
    #assert x+1==y,"test passed"
    assert x==y,"test failed"

def test_file1_method2():
    x=8
    y=6
    assert x+1==y,"test failed"
