"""Tasks"""

from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@app.task
def add(_x, _y):
    """Add function"""
    return _x + _y

@app.task
def subtract(_x, _y):
    """Subtract function"""
    return _x - _y
