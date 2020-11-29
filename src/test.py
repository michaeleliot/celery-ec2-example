from pytest import raises

from tasks import add

def test_add():
    math = add(1, 2)
    assert math == 3
