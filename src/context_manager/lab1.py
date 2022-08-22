# lab1
# Uzupełnij klase tak aby test wykorzystujący ją przeszedł poprawnie
# /tests/context_manager/test_lab1.py
# Zaimplementuj context manager za pomocą klasy

class MyContextManager:

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'__exit__({exc_type}, {exc_val}, {exc_tb})')
