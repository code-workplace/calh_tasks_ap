"""
Zaimplementuj dekorator, który sprawdzi, czy dekorowana funkcja ma zdefiniowane typingi (dla zmiennych oraz zwracanego obiektu)
Jeżeli brak jakiegokolwiek typingu, to udekorowana funkcja przy próbie wywołania nie powinna się wykonać,
powinna natomiast zwrócić string, z komunikatem:
"add typings to function <nazwa_funkcji>, please!"
gdzie nazwa_funkcji jest nazwą dekorowanej funkcji.
"""
from functools import wraps


def require_typing(fn):
    pass
