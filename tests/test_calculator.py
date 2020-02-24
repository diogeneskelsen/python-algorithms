"""Calculator tests

Unit tests for calculator utility methods.
"""

__author__ = "diogeneskelsen@gmail.com (Diogenes Kelsen)"

import unittest
from calculator.even import Even

TEST_CASES = [
    # (message, input, expected)
    ("Calculator output is wrong", [42, 11, 1, 2018], [0, 3, 1, 2]),
]


class TestCalculatorEven(unittest.TestCase):
    def test_base(self):
        calculator = Even()
        for (msg, n_list, expected) in TEST_CASES:
            self.assertEqual(calculator.new_input(n_list=n_list), expected, msg=msg)

if __name__ == "__main__":
    unittest.main()
