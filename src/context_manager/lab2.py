# lab2
# Zadanie polega wykorzystaniu context managera jako timera. Tak uzupełnij poniższa klasę aby przeszedł test
# /tests/context_manager/test_lab2.py

class Timer:
    def __init__ (self):
        self.time = 1
        print("init")
        
    def __enter__(self):
        print("enter")
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")





