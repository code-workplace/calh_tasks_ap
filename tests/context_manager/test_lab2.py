import time

from context_manager.lab2 import Timer

def test_timer():

    with Timer() as timer:
        time.sleep(1)

    assert timer.time == 1

