# test_calculate.py

import unittest
from calculate2 import calculate


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
