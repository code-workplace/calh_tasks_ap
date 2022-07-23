## Iteratory

### Iteracja
Na początek przypomnijmy sobie ważne pojecie jakim jest iteracja. Z iteracją już się wcześniej 
zetknęliśmy, iterowaliśmy po różnych obiektach - listach krotkach i zbiorach, przypomnijmy 
sobie zatem iteracje po tych obiekatch:

```
accounts_list = ["0000", "1111", "2222"]

print("iteracja po liście")
for account in accounts_list:
    print(account)
```
```
accounts_tuple = ("0000", "1111", "2222")

print("iteracja po krotce")
for account in accounts_tuple:
    print(account)
```
```
accounts_set = {"0000", "1111", "2222"}

print("iteracja po zbiorze")
for account in accounts_set:
    print(account)
```

### Iterator
Z iteratorami wiążą się 2 metody:
- ```__iter__()```, która zwraca iterator,
- ```__next__()```, która określa co się dzieje przy następnej iteracji po danym iteratorze.
 
Odpowiadają im funcje:
```iter()``` oraz ```next()```

- ```iter(obj)``` jest odpowiednikiem ```obj.__iter__()```, a
- ```next(it)``` jest odpowiednikiem  ```it.__next__()```.
```
accounts_list = ["0000", "1111", "2222"]

print("Typ accounts_list:", type(accounts_list))
# nie wykona się, bo nie mamy doczynienia z iteratorem
print(next(accounts_list))
```
```
accounts_list = ["0000", "1111", "2222"]

# tworzymy iterator dla accounts_list
accounts_list_iter = iter(accounts_list)
print("Typ accounts_list_iter:", type(accounts_list_iter))

print("Pierwsze wykonanie funkcji next():", next(accounts_list_iter))
print("Drugie wykonanie funkcji next():", next(accounts_list_iter)
```

###Własny iterator
Jeśli chcemy, żeby obiekt danej klasy był iterowalny musimy zaimplementować metodę ```__iter__()```.
```
class MyAccountList:
    accounts: list
    
    def __init__(self):
        self.accounts = list()

    def add_account(self, account: str):
        self.accounts.append(account)
        
    # za pomocą implementacji metody __iter__(), sprawiamy, że obiekt klasy MyAccountList 
    # może być iterowalny
    def __iter__(self):
        return iter(self.accounts)
```
```
myAccountList = MyAccountList()
myAccountList.add_account("0000")
myAccountList.add_account("1111")
myAccountList.add_account("2222")

from collections.abc import Iterable
isinstance(myAccountList, Iterable)

for account in myAccountList:
    print(account)
```

Jeśli nie tylko chcemy, żeby obiekt naszej klasy był iterowaly, ale również, chcemy zmodyfikować to 
co będzie zwracane przez iterator przy iteracji, musimy doimplementować metodę ```__next__()```. 
Należy pamiętać, że metoda ```__next__()``` działa na iteratorze.
```
class MyAccountList:
    accounts: list
    
    def __init__(self):
        self.accounts = list()

    def add_account(self, account: str):
        if len(self.accounts) == 0:
            current_id = 0
        else:
            last_id = self.accounts[-1]["id"]
            current_id = last_id + 1
        self.accounts.append({"id": current_id, "account": account})

    def __iter__(self):
        self.__accounts_iterator = iter(self.accounts) 
        return self

    def __next__(self):
        while True:
            account = next(self.__accounts_iterator)
            if (account["id"] % 2) == 0:
                return account["account"]


```
```
myAccountList = MyAccountList()

myAccountList.add_account("0000")
myAccountList.add_account("1111")
myAccountList.add_account("2222")
myAccountList.add_account("3333")

for account in myAccountList:
    print(account)
```