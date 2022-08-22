# """
# Zaimplementuj dekorator klas, który automatycznie uzupełni docstringi wszystkich utworzonych metod w dekorowanej klasie.
# Tekst, którym zostaną uzupełnione docstringi będzie przekazywany jako parametr do dekoratora (funkcji tworzącej dekoratory).
# Nie zmieniaj docstringów metod specjalnych (takich jak __init__, czy __repr__).
# """
def deco_doc(new_docstring):
    def dec(cls):
        method_list = [attribute for attribute in dir(cls) if
                       callable(getattr(cls, attribute))
                       and attribute.startswith('__') is False]

        for method in method_list:
            getattr(cls, method).__doc__ = new_docstring
        return cls
    return dec