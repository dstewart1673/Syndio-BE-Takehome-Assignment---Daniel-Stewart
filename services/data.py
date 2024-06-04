import sqlite3
import os
import pandas as pd

def get_employees(department):
    '''Takes an optional department name and returns the compensation, protected_class, tenure, and performance of all employees as a mutidimensional list'''

    with sqlite3.connect(os.path.abspath('database/employees.db')) as conn:

        query = 'SELECT * FROM employees' if department is None else "SELECT * FROM employees WHERE department = '?" + department + "'"
        df = pd.read_sql_query(query, conn)

        return df