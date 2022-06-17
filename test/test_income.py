import sys
import os
from pytest import MonkeyPatch
sys.path.insert(0, os.path.abspath(os.curdir))

from src import income

def test_income_expense(monkeypatch: MonkeyPatch) -> None:
    """Test values: 
        income01 = 10,000 ; income02 = 45,856.45; income03 = 0.78
        recall that  -> expenses = 80% of income
                        saving   = 20% of income
    """
    inputs = ["10000", "45856.45", "0.78"]
    expected_values = [(0.8 * 10000 , 0.2 * 10000), 
                      (0.8 * 45856.45, 0.2 * 45856.45),
                      (0.8 * 0.78, 0.2 * 0.78)]
    for values in expected_values:
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        assert income.income_expense() == values

