import unittest
from main import add_numbers

class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(5, 5), 10)

    def test_add_numbers_negative(self):
        self.assertEqual(add_numbers(-1, -2), -3)
        self.assertEqual(add_numbers(-5, -5), -10)

if __name__ == '__main__':
    unittest.main()