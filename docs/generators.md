##Generatory
Generator jest pewnym specyficznym rodzajem funkcji (lub wyrażenia), która po zwróceniu elementu zapamiętuje 
swój stan. Funkcja ta może zostać wstrzymana oraz wznowiona od miejsca, w którym została wstrzymana.

Generatory cechuje leniwa ewaluacja (ang. lazy evaluation), czyli tworzenie kolejnych elementów 
dopiero przy odwołaniu się do generatora. Pozwala to zredukować liczbę wykonywanych obliczeń, 
zmniejszyć wykorzystanie pamięci oraz tworzyć nieskończoną ilość elementów.

###Tworzenie generatora (funkcji generującej)

```
def moj_pierwszy_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
```
```
g = moj_pierwszy_generator()
print("Pierwszy element generatora:", next(g))
print("Drugi element generatora:", next(g))
```
Możemy również stworzyć listę z generatora, natomiast trzeba pamiętać, że jeśli już wcześniej 
iterowaliśmy po tym generatorze, to dostaniemy listę elementów od ostatniego stanu.
```
print(list(g))
```
Jeśli chcemy pełną listę musimy utworzyć generator od nowa.
```
g = moj_pierwszy_generator()
print(list(g))
```
###Funkcja generująca, a standardowa
Stwórzmy funkcję ```numbers_normal``` zwracającą ciąg cyfr od 0 do n, podniesionych do kwadratu.
```
def numbers_normal(n):
    output = list()
    for i in range(n):
        output.append(i**2)
    return output
    
for even in numbers_normal(10):
    print(even)
```
Teraz stwórzmy odpowiednik funkcji ```numbers_normal``` - funkcję generującą ```numbers_generator```
Tworzenie funkcji generującej nie różni się znacznie od standardowej, poza tym, że zamiast ```return```
stosujemy ```yield```, nie musimy też tworzyć listy do której przypisujemy kolejne wartości, ponieważ 
generator pamięta poprzedni stan.
```
def numbers_generator(n):
    for i in range(n):
        yield i**2

for even in numbers_generator(10):
    print(even)
```

###Wyrażenie generujące
Możemy również stworzyć odpowiednik wyrażenia listowego - wyrażenie generujące.
```
list_comprehension = [i**2 for i in range(10+1)]
```
Wyrażenie generujące tworzymy w identyczny sposób co listowe, z tym, że zamiast nawiasów ```[]```, 
stosujemy ```()```.
``` 
generator_comprehension = (i**2 for i in range(10+1)
```

