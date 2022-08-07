# lab4
# Napisz manager contextu wspierający operacje na bazie danych w naszym przypadku sqllite
# https://docs.python.org/3/library/sqlite3.html
# /tests/context_manager/test_lab3.py

from contextlib import contextmanager

class MyContextManagerClass:
    
    def __init__ (self):
        print("init")
        
    def execute(*args, **kwargs):
        print("execute")
        
    def fetchall(self):
        print("fetchall")
        

@contextmanager
def open_db(file_name: str):
    yield MyContextManagerClass()





