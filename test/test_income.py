import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.curdir))

import typing
from src import income
class TestCalc(unittest.TestCase):
    def test_income_expense(self):
        income01: int = 10000; income02: float = 10000.49
        self.assertEqual(income.income_expense(), (0.8*income01, 0.2*income01))
        self.assertEqual(income.income_expense(), (0.8*income02, 0.2*income02))
# def test_income_expense():
#     assert income.income_expense() == (80, 20)
#     assert income.income_expense() == (800.08, 200.02)

if __name__ == '__main__':
    unittest.main()