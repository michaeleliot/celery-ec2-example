"""
Example celery
"""
from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@app.task
def add(_x, _y):
    """Sum y from x"""
    return _x + _y

@app.task
def subtract(_x, _y):
    """Subtract y from x"""
    return _x - _y
