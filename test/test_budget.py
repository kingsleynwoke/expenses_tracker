import sys
import os
from pytest import MonkeyPatch
import numpy as np
sys.path.insert(0, os.path.abspath(os.curdir))
from src import budget

def test_check_budget(monkeypatch: MonkeyPatch) -> None:
    expenses_type = ["cosmetic", "party", "charity", "grocery",
                     "clothing", "transport", "insurance", "misc"]
    
    for key in expenses_type:
        monkeypatch.setattr("builtins.input", lambda _: "45856.45")
        assert type(budget.check_budget()) is dict
        assert key in budget.check_budget()
        assert type(budget.check_budget()[key]) is np.float64