## Context manager

Zarządzanie zasobami to jedna z tych rzeczy, które musisz zrobić w każdym języku programowania. Czy to jest otwieranie plików,
czy zarządzenie sesjami czy połączeniami z bazą danych czy uzyskanie blokady stanu to zawsze należy zadbać z zamknięcie i zwolnienie zasobów. 


W python mamy już do tego ``try/finally`` ale context manager to coś więcej, przede wsszystkim poprawia czytelność kodu ale daje eż gwarancję
że programista nie zapomni o zwolnieniu zasobów.


Implemetujemy go za pomocą instrukcji ``with``. Uzycie jej gwarantuje nam, że jakaś operacja zostanie wykonana na końcu,
nawet jeśli wystąpi wyjątek lub zakończenie programu.


---
### 1. Prosty przykład otwarcie pliku

Poniżej trzy podejścia, oczywiście najlepsze to te wykorzystujace context manager :)

- **Uwaga !!!!!** Zadziała ale tak nie piszemy, poniważ jeżeli wsytąpi błąd podczas czytania pliku nie wykona się instrukcji f.close() co spowoduje że zasoby nie zostaną zwolnione.
```
f = open('/path/to/file.txt', 'r')
for line in f:
    print(line)
f.close()  # trzeba o tym pamiętać
```

- Tak jest dobrze
```
f = open('/path/to/file.txt', 'r')
try:
  for line in f:
    print(line)
finally:
  f.close() 
```

 - A tak super, zwięźle i czysto a cała konfiguracja dostępu do zasobu tutaj do pliku została zamknięta w context manager za pomocą instrukcji ``with``
```
with open('/path/to/file.txt', 'r') as f:
  for line in f:
    print(line)
```

---

### 2. Jak zaimplementować menedżer kontekstu ?

Istnieją dwa sposoby na zaimplementowanie menedżera kontekstu.

 

- Pierwszy z nich jest zdefiniowanie klasy z implementacjami dla metod ```__enter__``` i ```__exit__```. Argumenty **exc_type, exc_val, exc_tb** w metodzie ```__exit__``` służą do przekazania informacji o potencjalnym wyjątku
```
class MyContextManager:

    def __init__(self):
        print('__init__')

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'__exit__({exc_type}, {exc_val}, {exc_tb})')

    def run(self):
        print('run')     
```

```
with MyContextManager() as cm:
    cm.run()
```

- Drugi to stworzenie generatora i użycie contextlib.contextmanager jako dekoratora.
```
from contextlib import contextmanager

class SomeClass:
    def run(self):
        print('run')

@contextmanager
def my_context_manager():
    print('Starting')
    try:
        yield SomeClass()
    except ValueError as e:
        print(e)
        print('Ignore exception')
    except Exception as e:
        print(e)
        print('Do not ignore exception')
        raise
    finally:
        print('Exiting')
```

```
with my_context_manager() as cm:
    cm.run()
```
---
### 3. Przydatne liniki
 - *[contextlib] <https://docs.python.org/3.10/library/contextlib.html>*



















