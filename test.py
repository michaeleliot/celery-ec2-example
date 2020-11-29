from pytest import raises

from tasks import add, subtract

def test_add():
    math = add(1, 2)
    assert math == 3

def test_add():
    math = subtract(2, 1)
    assert math == 1