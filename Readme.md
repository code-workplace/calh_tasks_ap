### Cześć praktyczna

Zadania znajdują się w pakiecie `/src` i zostały podzielone tematycznie na laby. Dla każdego lab jest napisany jego test w pakiecie `/tests`.
Należy uzupełnić tak kod zadania aby jego testy zakończyły się sukcesem czyli na zielono. 

---

**Przygotowanie repozytorium**

1. Utwórz nowe prywatne repozytorium za pomocą interfejscu użytkownika GitHub
``https://github.com/yourname/private-repo.git``

3. Wykonaj polecenia tworzące tymczasową kopię repozytorium z zadaniami

``git clone --bare https://github.com/code-workplace/calh_tasks_ap.git``

4. Przenieś kopię lustrzaną do nowego prywatnego repozytorium

```
cd calh_tasks_ap.git
git push --mirror https://<GITHUB_ACCESS_TOKEN>@github.com/yourname/private-repo.git
```

5. Usuń tymczasowe lokalne repozytorium
```
cd ..
rm -rf calh_tasks_ap.git
```

6. Sklonuj prywatne repozytorium, aby móc na nim pracować
```
git clone https://<GITHUB_ACCESS_TOKEN>@github.com/yourname/private-repo.git
cd private-repo
```
   << wprowadź zmiany >>
```
git commit
git push origin master
```

7. Aby móc aktualizować kod z repozytorium publicznego należy je dodać
```
cd private-repo
git remote add public https://github.com/code-workplace/calh_tasks_ap.git
git pull public master
git push origin master
```

---

**Kolejny krok to instalacja pakietu ```pytest``` potrzebnego do testów. Można to zrobić za pomocą narzędzia
```pycharm``` lub z terminala, tworząc środowisko wirtualne ```virtualenv```  i instalując wymagane zależności**

1. Z wiersza poleceń w katalogu projektu wykonaj komendę:

```python -m venv venv```

2. Następnie, aby aktywować środowisko wirtualne, wykonaj komendę:
```
(Windows) venv\Scripts\activate.bat
(Linux, MacOS X) source bin/activate
```

3. Zainstaluj zależności zdefiniowane w pliku `requirements.txt` przy pomocy komendy

``python -m pip install -r ./requirements.txt``


Jeśli wszystko przebiegło pomyślnie, możesz uruchomić testy wpisując:

```python -m pytest```


---




