import unittest

from src.iterators.HFWC import ClientsList


class clientsTest(unittest.TestCase):

    def test_length_0(self):
        clients = ClientsList()
        iterator = iter(clients)
        self.assertEqual(len(list(iterator)), 0)

    def test_length_more_than_0(self):
        clients = ClientsList()
        iterator = iter(clients)
        clients.add_client(pesel="000000")
        clients.add_client(pesel="100000")
        clients.add_client(pesel="200000")
        clients.add_client(pesel="300000")
        self.assertEqual(len(list(iterator)), 4)

    def test_length_remove_client(self):
        clients = ClientsList()
        iterator = iter(clients)
        clients.add_client(pesel="000000")
        clients.add_client(pesel="100000")
        clients.add_client(pesel="200000")
        clients.add_client(pesel="300000")
        clients.remove_client(pesel="200000")
        self.assertEqual(len(list(iterator)), 3)

    def test_iterator_values(self):
        clients = ClientsList()
        iterator = iter(clients)
        clients.add_client(pesel="000000")
        clients.add_client(pesel="100000")
        self.assertEqual(next(iterator), "000000")
        self.assertEqual(next(iterator), "100000")

    def test_iterator_values_after_remove_client(self):
        clients = ClientsList()
        iterator = iter(clients)
        clients.add_client(pesel="000000")
        clients.add_client(pesel="100000")
        clients.add_client(pesel="200000")
        clients.add_client(pesel="300000")
        clients.remove_client(pesel="100000")
        self.assertEqual(next(iterator), "000000")
        self.assertEqual(next(iterator), "200000")
        self.assertEqual(next(iterator), "300000")
