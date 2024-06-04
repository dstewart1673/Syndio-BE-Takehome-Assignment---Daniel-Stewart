from fastapi import FastAPI
from services.data import get_employees
from services.math import generate_pvalues
from models.pvalue import PValueResponse


app = FastAPI()

@app.get("/pvalue")
def get_pvalue(department: str = None) -> PValueResponse:
    employee_values = get_employees(department)

    # converting protected class to numeric for use as a non-categorical variable in the regression
    employee_values['protected_class'] = employee_values['protected_class'].apply(lambda x: 0 if x == 'reference' else 1)
    
    x_vals = employee_values[['protected_class', 'tenure', 'performance']]
    y_vals = employee_values['compensation']
    pvals = generate_pvalues(x_vals, y_vals)

    return PValueResponse(pvalue=pvals['protected_class'].round(3))