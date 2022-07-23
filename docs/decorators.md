<h1 id="decorators">decorators</h1>

<h2 id="table_of_contents">spis treści</h2>

[dekoratory - podstawy](#decorators_basics)
* [definicja](#decorator_definition)
* [składnia](#decorators_syntax)
* [wraps](#wraps)

[przykłady](#decorators_examples)
* [counter](#counter)
* [logger](#logger)
* [timer](#timer)

[łączenie dekoratorów](#stacking_decorators)
* [składnia](#stacking_decorators_syntax)

[dekoratory z paramterami](#decorator_with_parameters)

[klasa dekorator](#decorator_class)

[dekorowanie klas](#decorating_classes)

[dekoratory standardowej biblioteki pythona](#std_lib_decorators)
* [functools](#functools)
* [dataclasses](#dataclasses)
* [contextlib](#contextlib)

[dekoratory programowania obiektowego](#oop_decorators)
* [property](#property)
* [static_method](#static_method)
* [class_method](#class_method)


<h2 id="decorators_basics">dekoratory - podstawy</h2>


<h3 id="decorator_definition">definicja</h3>

* Dekorator - obiekt, którego argumentem jest obiekt
* Python 2.4: PEP 318 -- Decorators for Functions and Methods
* Python 3.9: PEP 614 -- Relaxing Grammar Restrictions On Decorators
* dekorator może:
  * wykonywać dodatkowe funkcjonalności przed wywołaniem funkcji
  * wykonywać dodatkowe funkcjonalności po wywołaniu funkcji
  * modyfikować argumenty
  * modyfikować zwracaną wartość
  * zaniechać wywołania
  * modyfikować zmienne globalne
  * dodawać lub zmieniać metadane
* dekorować możemy:
  * funkcje
  * metody
  * klasy


<h3 id="decorators_syntax">składnia</h3>

Tworzenie dekoratora:
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        pass
        return func(*args, **kwargs)
    return wrapper
```

Dekorowanie fukcji:
```python
def func():
    pass

decorated_func = decorator(func)
```

Dekorowanie funkcji w momencie jej definiowania, skrócona składnia (PEP 318):
```python
@decorator
def decorated_func():
    pass
```

Konsekwencje:
* udekorowana funkcja nie jest już tą samą funkcją
* adres w pamięci zostaje zmieniony
* nazwa, docstringi, annotacje przepadają

<h3 id="example">przykład</h3>

```python
def counter(fn):
    count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{fn.__name__} was called {count} times')
        return fn(*args, **kwargs)
    return wrapper


@counter
def square(n):
    return n**2

for i in range(3):
    print(square(i))
    
print(square.__name__)
print(square.__doc__)
```

```python
# extract function name and doctstrings and add to wrapper
def counter(fn):
    count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{fn.__name__} was called {count} times')
        return fn(*args, **kwargs)
    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper


@counter
def square(n):
    """
    return square value of n
    """
    return n**2

for i in range(3):
    print(square(i))
    
print(square.__name__)
print(square.__doc__)
```

<h3 id="wraps">wraps</h3>

* functools.wraps
* dekorator, który wywołuje funkcję functools.update_wrapper() na funkcji wewnętrznej dekoratora
* aktualizuje dekorowaną funkcję, żeby wyglądała jak funkcja oryginalna

```python
from functools import wraps

def counter(fn):
    count = 0
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{fn.__name__} called {count} times')
        return fn(*args, **kwargs)
    return wrapper


@counter
def square(n):
    """
    return square value of n
    """
    return n**2

for i in range(3):
    print(square(i))
    
print(square.__name__)
print(square.__doc__)
```


<h2 id="decorators_examples">przykłady</h2>


<h3 id="counter">counter</h3>

```python
from functools import wraps

def counter(fn):
    count = 0
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{fn.__name__} called {count} times')
        return fn(*args, **kwargs)
    return wrapper
```

<h3 id="logger">logger</h3>

```python
from functools import wraps
from datetime import datetime
    
def logged(fn):   
    @wraps(fn)
    def wrapper(*args, **kwargs):
        run_dt = datetime.now()
        result = fn(*args, **kwargs)
        print(f'{fn.__name__}: called {run_dt}')
        return result
        
    return wrapper
```

<h3 id="timer">timer</h3>

```python
from datetime import datetime
from functools import wraps


def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = fn(*args, **kwargs)
        end = datetime.now()
        elapsed = (end - start).seconds

        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ', '.join(all_args)
        print(f'{fn.__name__}({args_str}) took {elapsed:.6f}s to run.')
        return result

    return wrapper
```


<h2 id="stacking_decorators">łączenie dekoratorów</h2>

<h3 id="stacking_decorators_syntax">składnia</h3>

```python
@decorator_1
@decorator_2
def function_1():
    pass
```

```python
def function():
    pass

function = decorator_1(decorator_2(function))
```

* łączenie funkcjonalności kilku dekoratorów
* stacking, chaining dekoratorów - dekorowanie udekorowanej funkcji
* kolejność dekorowania może mieć znaczenie
* przykładowo - autentyfikacja użytkownika vs wykonanie zapytania na bazie danych

```python
from counter import counter
from logger import logged

@counter
@logged
def add_1(a, b):
    return a + b

def add_2(a, b):
    return a + b

add_2 = counter(logged(add_2))

if __name__ == '__main__':
    for i in range(10):
        print(add_1(1, i))
        print(add_2(1, i))
```

<h2 id="decorator_with_parameters">dekoratory z parametrami</h2>

Tworzenie dekoratora z parametrami:
* wykorzystanie zewnętrznej funkcji, która przy wywołaniu zwraca dekorator
* argumenty przekazywane są do tej zewnętrznej funkcji
* dekorator i jego funkcja wewnętrzna mogą korzystać z przekazanych argumentów jako zmiennych nonlocal

```python
def dec_factory(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('running decorator inner')
            print('free vars: ', a, b)
            return fn(*args, **kwargs)
        return inner
    return dec     
```

```python
from datetime import datetime

def timed_factory(num_reps=1):
    def timed(fn):

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = datetime.now()
                result = fn(*args, **kwargs)
                end = datetime.now()
                total_elapsed += (end - start).seconds
            avg_elapsed = total_elapsed / num_reps
            print(f'Avg Run time: {avg_elapsed:.6f}s ({num_reps} reps)')
            return result
        return inner
    return timed       
```


<h2 id="decorator_class">klasa dekorator</h2>

```python
class Origin:
    def __init__(self, x, y):
        self.origin_x = x
        self.origin_y = y
        
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f'origin = ({self.origin_x}, {self.origin_y})')
            return fn(*args, **kwargs)
        return inner
```

```python
@Origin(0, 0)
def calculate_distance(s):
    print(f'calculating distance')

calculate_distance((3, 4))
```


<h2 id="decorating_classes">dekorowanie klas</h2>

* dekorowanie klasy:
  * przekazanie klasy do dekoratora
  * modyfikacja klasy
  * zwrócenie zmodyfikowanej/udekorowanej klasy
* przykładowa dekoracja klasy:
  * dodanie atrybutu
  * dodanie metody

```python
from datetime import datetime

def debug_info(cls):
    def info(self):
        results = list()
        results.append(f'time: {datetime.now()}')
        results.append(f'class: {self.__class__.__name__}')
        results.append(f'id: {hex(id(self))}')
        
        if vars(self):
            results.extend(f'{k}: {v}' for k, v in vars(self).items())
            
        return results
    
    cls.debug = info
    
    return cls
```

```python
@debug_info
class Student:
    def __init__(self,
                 first_name,
                 last_name,
                 age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def say_hello(self):
        print(f'Hello, my name is {self.first_name} {self.last_name}')
    
user = Student('Jan', 'Twardowski', 33)
user.debug()
```


<h2 id="std_lib_decorators">dekoratory biblioteki standardowej</h2>

<h3 id="functools">functools</h3>

* wraps
* lru_cache
* total_ordering


<h4 id="lru_cache">lru_cache</h4>

* functools.lru_cache
* least-recently-used cache - dekorator zapisujący wyniki ostatnich wywołań funkcji, w celu ponownego ich użycia

```python
# recursive fib
def fib(n):
    print (f'calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(9)
```

```python
# recursive fib with caching
from functools import wraps

def cache_fib(fn):
    cache = dict()
    
    @wraps(fn)
    def wrapper(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    
    return wrapper


@cache_fib
def fib(n):
    print (n'calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(9)
```

```python
# recursive fib with lru_caching
from functools import lru_cache

@lru_cache
def fib(n):
    print(f'calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(9)
```

<h4 id="total_ordering">total_ordering</h4>

* functools.total_ordering
* dekorator klasy
* dla danej klasy posiadającej zdefiniowaną jedną lub więcej metod specjalnych porównujących instancje klasy (np. \_\_lt__()), uzupełnia klasę o pozostałe metody porównujące
* klasa musi mieć zdefiniowaną jedną z metod \_\_lt__(), \_\_le__(), \_\_gt__(), lub \_\_ge__() oraz dodatkowo metodę \_\_eq__()

```python
from functools import total_ordering

@total_ordering
class Square:
    def __init__(self, a):
        self.a = a
    
    @property
    def area(self):
        return self.a ** 2
     
    def __repr__(self):
        return f'Square({self.a})'
    
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area == other.area
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area > other.area
        else:
            return NotImplemented
```

```python
s1, s2 = Square(2), Square(5)
print(f'{repr(s1)} == {repr(s2)}, {s1 == s2}')
print(f'{repr(s1)} != {repr(s2)}, {s1 != s2}')
print(f'{repr(s1)} < {repr(s2)}, {s1 < s2}')
print(f'{repr(s1)} <= {repr(s2)}, {s1 <= s2}')
print(f'{repr(s1)} > {repr(s2)}, {s1 > s2}')
print(f'{repr(s1)} >= {repr(s2)}, {s1 >= s2}')
```


<h3 id="dataclasses">dataclasses</h3>

* dataclasses.dataclass
* dekorator klasy
* PEP 557 – Data Classes
* https://docs.python.org/3/library/dataclasses.html
* automatycznie dodaje metody specjalne, takie jak __init__(), __repr__() do dekorowanej klasy

````python
from dataclasses import dataclass

@dataclass
class Student:
    first_name: str
    last_name: str
    age: int = 0

    def say_hello(self):
        print(f'Hello, my name is {self.first_name} {self.last_name}')
        
        
student = Student('Jan', 'Twardowski')
print(student)
student.say_hello()
````

<h3 id="contextlib">contextlib</h3>
* contextlib.contextmanager


<h3 id="oop_decorators">OOP decorators</h3>

* property
* classmethod
* staticmethod
* abc.abstractmethod
