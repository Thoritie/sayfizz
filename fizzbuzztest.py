import unittest

from utils import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_input_3_should_return_fizz(self):
        actual = fizzbuzz(3)
        self.assertEqual(actual, 'fizz')

unittest.main()
