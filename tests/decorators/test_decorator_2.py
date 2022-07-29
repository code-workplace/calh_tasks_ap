import unittest

from src.decorators.decorator_2 import deco_doc


class RequireTypingTest(unittest.TestCase):

    def test_is_callable(self):
        text = 'They told me to write docstrings'

        @deco_doc(text)
        class Employee:
            def __init__(self, first_name, last_name, salary):
                self.first_name = first_name
                self.last_name = last_name
                self.salary = salary

            def increase_salary(self, amount):
                self.salary += amount

            def get_salary(self):
                return self.salary

        self.assertEqual(Employee.increase_salary.__doc__, text)
        self.assertEqual(Employee.get_salary.__doc__, text)
        self.assertNotEqual(Employee.__init__.__doc__, text)
