### Cześć praktyczna

Zadania znajdują się w pakiecie `/src` i zostały podzielone tematycznie na laby. Dla każdego lab jest napisany jego test w pakiecie `/tests`.
Należy uzupełnić tak kod zadania aby jego testy zakończyły się sukcesem czyli na zielono. 

**Przygotowanie środowiska** 

---

1. Forkowanie repozytorium z zadaniami, sprowadza się do jednego kliknięcia nad repozytorium do którego mamy dostęp, wystarczy kliknąć przycisk `fork`.
Dzięki temu uzyskamy kopię repozytorium całkowicie pod naszą kontrolą.

2. Kolejny krok to utworzenie i skonfigurować środowisko wirtualne virtualenv. 
Aby to zrobić, najpierw z wiersza poleceń w katalogu projektu wykonaj komendę:
`python -m venv venv`

3. Następnie, aby aktywować środowisko wirtualne, wykonaj komendę:
```
(Windows) venv\Scripts\activate.bat
(Linux, MacOS X) source bin/activate
```

4. Zainstaluj zależności zdefiniowane w `pliku requirements.txt` przy pomocy komendy

``python -m pip -f ./requirements.txt``


Jeśli wszystko przebiegło pomyślnie, możesz uruchomić testy wpisując:

```python -m pytest```


---




