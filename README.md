#### **ReDI School of Digital Integration**
**Semester:** Spring 2022 <br>
**Course:** Python Foundation Semester Project <br>
**Topic:** Expenses Tracker

The aim of this program is to track expenses across sets of user-defined categories of expenses.
The programe dependencies are listed in the requirements.txt.

**Note:** <br>

1. To visualize the data in nice looking figure kindly install SciencePlots <br>
1. Latex needs to be installed first before installing it <br>
1. The installation guide can be found in [installation page](https://pypi.org/project/SciencePlots/)

#### Below shows the scripts dependency
1.  **income.py**, **read_file.py** and **generate_expenses.py**
    - import user_validation.py
1.  **sum_expenses_data.py**
    - import income.py and read_file.py
1.  **budget.py** 
    - import sum_expenses_data.py, user_validation.py and income.py
1.  **plotting.py**
    - import budget.py and sum_expenses_data.py
1.  **main_function.py**
    - import generate_expenses.py and read_file.py
    - import sum_expenses.py and plotting.py

The main_function.py script is the calling or main function for the program.