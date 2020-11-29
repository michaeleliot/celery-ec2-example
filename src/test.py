"""
Example celery test
"""
from tasks import add, subtract

def test_add():
    """Add test"""
    math = add(1, 2)
    assert math == 3

def test_subtract():
    """Subtract test"""
    math = subtract(2, 1)
    assert math == 1
