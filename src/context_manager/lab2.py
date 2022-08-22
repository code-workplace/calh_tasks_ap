# lab2
# Zadanie polega wykorzystaniu context managera jako timera. Tak uzupełnij poniższa klasę aby przeszedł test
# /tests/context_manager/test_lab2.py

import time


class Timer:
    def __init__(self):
        self.time = None
        self.enter = None
        self.exit = None

    def __enter__(self):
        self.enter = int(time.time())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit = int(time.time())
        self.time = self.exit-self.enter

        return self
