"""
Klasa ClientsList, obsługuje bazę klientów, baza zawiera informacje o tym jaki jest
numer pesel klienta, oraz czy jest aktywnym klientem, jej funkcjonalności są następujące:

     - Metoda add_client przyjmuje za argument numer pesel, powoduje dodanie klienta do
     listy klientów wraz z przypisaniem mu wartości True do flagi is_active
    - Metoda remove_client przyjumuje za argument numer pesel i zmienia wartośc flagi
    is_active na False nie powoduje usunięcia rekordu dla
    - Zadanie polega na zaimplenentowaniu metod dzięki którym podczas iterowania po
    obiekcie klasy ClientsList będą zwracane tylko numery pesel dla osób które są
    aktywnymi klientami (wartość flagi is_active to True)
"""


class ClientsList:
    clients: list

    def __init__(self):
        self.clients = list()

    def add_client(self, pesel: str):
        self.clients.append({"pesel": pesel, "is_active": True})

    def remove_client(self, pesel: str):
        for i in range(0, len(self.clients)):
            if self.clients[i]["pesel"] == pesel:
                self.clients[i]["is_active"] = False
                break
                
    def __iter__(self):
        self.__clients_iterator = iter(self.clients)
        return self
                
    def __next__(self):
        while True:
            client = next(self.__clients_iterator)
            if client["is_active"] == True:
                return client["pesel"]
