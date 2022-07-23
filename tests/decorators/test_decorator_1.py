import unittest

from src.decorators.decorator_1 import require_typing


class RequireTypingTest(unittest.TestCase):

    def test_is_callable(self):
        self.assertEqual(callable(require_typing), True)

    def test_good_typing(self):
        @require_typing
        def add(a: float, b: float) -> float:
            return a + b
        self.assertEqual(add(1, 2), 3)

    def test_good_typing_syntax(self):
        def add(a: float, b: float) -> float:
            return a + b
        add = require_typing(add)
        self.assertEqual(add(1, 2), 3)

    def test_non_typing_vars(self):
        @require_typing
        def add(a, b) -> float:
            return a + b
        self.assertEqual(add(1, 2), f'Add typing to function add, please!')

    def test_non_typing_return(self):
        @require_typing
        def add(a: float, b: float):
            return a + b
        self.assertEqual(add(1, 2), f'Add typing to function add, please!')
