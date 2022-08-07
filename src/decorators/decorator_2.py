"""
Zaimplementuj dekorator klas, który automatycznie uzupełni docstringi wszystkich utworzonych metod w dekorowanej klasie.
Tekst, którym zostaną uzupełnione docstringi będzie przekazywany jako parametr do dekoratora (funkcji tworzącej dekoratory).
Nie zmieniaj docstringów metod specjalnych (takich jak __init__, czy __repr__).
"""

def deco_doc(new_docstring):
    def decorator(fn): 
        for i in dir(fn):
            if i[0:2] != "__":
                
                setattr(fn, i.__doc__, new_docstring)   
                #setattr(getattr(fn, i), '__doc__', new_docstring)   
       
        def wrapper(*args, **kwargs):                            
            result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorator
