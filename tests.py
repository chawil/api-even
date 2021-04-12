import unittest
from random import randint

from core import is_even
from core import is_odd


class TestEvenCore(unittest.TestCase):

    def test_is_1_even(self):
        self.assertFalse(is_even(1))

    def test_is_2_even(self):
        self.assertTrue(is_even(2))        

    def test_is_1_odd(self):
        self.assertTrue(is_odd(1))

    def test_is_2_odd(self):
        self.assertFalse(is_odd(2))        

    def test_random_small_number(self):
        for _ in range(9):
            random_int = randint(0, 9)
            even = random_int % 2 == 0
            self.assertEqual(is_even(random_int), even)
            odd = random_int % 2 == 1
            self.assertEqual(is_odd(random_int),odd)



if __name__ == '__main__':
    unittest.main()
