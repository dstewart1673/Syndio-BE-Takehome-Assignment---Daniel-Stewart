import sqlite3
import os
import pandas as pd

def get_employees(department: str = None):
    '''Takes an optional department name and returns the compensation, protected_class, tenure, and performance of all employees as a mutidimensional list'''

    with sqlite3.connect(os.path.abspath('database/employees.db')) as conn:

        query = 'SELECT * FROM employees WHERE ' if department is None else "SELECT * FROM employees WHERE department = '" + department + "' AND "
        
        # don't want to include incomplete records for now. if a use case comes up this can be moved behind a flag.
        query += "'protected_class' IS NOT NULL AND 'tenure' IS NOT NULL AND 'performance' IS NOT NULL AND 'compensation' IS NOT NULL"

        df = pd.read_sql_query(query, conn)

        return df