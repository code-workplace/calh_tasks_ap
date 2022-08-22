# """
# Zaimplementuj dekorator, który sprawdzi, czy dekorowana funkcja ma zdefiniowane typingi (dla zmiennych oraz zwracanego obiektu)
# Jeżeli brak jakiegokolwiek typingu, to udekorowana funkcja przy próbie wywołania nie powinna się wykonać,
# powinna natomiast zwrócić string, z komunikatem:
# "add typings to function <nazwa_funkcji>, please!"
# gdzie nazwa_funkcji jest nazwą dekorowanej funkcji.
# """
from inspect import signature


def require_typing(func):
    def wrapper(*args, **kwargs):
        func_signature = signature(func)

        if func_signature.return_annotation is func_signature.empty:
            return f'Add typing to function {func.__name__}, please!'

        for parameter in func_signature.parameters.items():
            if parameter[1].annotation is func_signature.empty:
                return f'Add typing to function {func.__name__}, please!'

        return func(*args, **kwargs)
    return wrapper
