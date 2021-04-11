import unittest
from random import randint

from core import is_even


class TestEvenCore(unittest.TestCase):

    def test_is_1_even(self):
        self.assertFalse(is_even(1))

    def test_random_small_number(self):
        for _ in range(9):
            random_int = randint(0, 9)
            even = random_int % 2 == 0
            self.assertEqual(is_even(random_int), even)


if __name__ == '__main__':
    unittest.main()
