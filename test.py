"""Tests"""
from tasks import add, subtract

def test_add():
    """Test add function"""
    math = add(1, 2)
    assert math == 3

def test_subtract():
    """Test subtract function"""
    math = subtract(2, 1)
    assert math == 1
