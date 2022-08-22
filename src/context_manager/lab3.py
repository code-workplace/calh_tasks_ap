# lab4
# Napisz manager contextu wspierający operacje na bazie danych w naszym przypadku sqllite
# https://docs.python.org/3/library/sqlite3.html
# /tests/context_manager/test_lab3.py

import sqlite3 as sql
from contextlib import contextmanager

@contextmanager
def open_db(file_name: str):
    try:
        con = sql.connect(file_name)
        yield con.cursor()
    except ConnectionError as e:
        print(e)
        print('Błąd połączenia z bazą')
        raise
    finally:
        con.close()





