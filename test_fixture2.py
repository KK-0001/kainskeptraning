import pytest

@pytest.fixture()
def setup():
    print("this is the fixture method 1")
@pytest.fixture()
def setup2():
    print("this is fixture method 2")
    
    
def test_method1(setup):
    print("test case 1")

def test_method2(setup):
    print("test case 2")

def test_method3(setup2):
    print("test case 3")
