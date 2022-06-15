import sys
import os
sys.path.insert(0, os.path.abspath(os.curdir))

import typing

from redi_project.src import income
income.income_expense()
