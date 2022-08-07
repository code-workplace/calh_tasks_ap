"""
Zaimplementuj dekorator, który sprawdzi, czy dekorowana funkcja ma zdefiniowane typingi (dla zmiennych oraz zwracanego obiektu)
Jeżeli brak jakiegokolwiek typingu, to udekorowana funkcja przy próbie wywołania nie powinna się wykonać,
powinna natomiast zwrócić string, z komunikatem:
"add typings to function <nazwa_funkcji>, please!"
gdzie nazwa_funkcji jest nazwą dekorowanej funkcji.
"""
from functools import wraps

def require_typing(func):    
    @wraps(func)
    def wrapper(*args, **kwargs):
        if (len(func.__annotations__) != len(func.__code__.co_varnames) + 1):
            return "Add typing to function " + func.__name__ +", please!"
        else:
            result = func(*args, **kwargs)
            return result
    return wrapper



