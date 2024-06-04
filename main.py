from fastapi import FastAPI, HTTPException
from services.data import get_employees
from services.math import generate_pvalues
from models.pvalue import PValueResponse
from models.departments import Department


app = FastAPI()

@app.get("/pvalue")
def get_pvalue(department: str = None) -> PValueResponse:
    
    try:
        # simplistic parameter safety check for this limited data set. should be made more flexible/robust if opening up to more varied data sets/outside entities.
        if not department is None and not department in Department:
            raise HTTPException(status_code=400, detail='Invalid department name')

        employee_values = get_employees(department)

        # converting protected class to numeric for use as a non-categorical variable in the regression
        employee_values['protected_class'] = employee_values['protected_class'].apply(lambda x: 0 if x == 'reference' else 1)
        
        x_vals = employee_values[['protected_class', 'tenure', 'performance']]
        y_vals = employee_values['compensation']
        pvals = generate_pvalues(x_vals, y_vals)

        return PValueResponse(pvalue=pvals['protected_class'].round(3))
    except HTTPException as err:
        raise err
    except:
        #TODO: Add logging/alerting here so we know when somthing's failing unexpectedly

        raise HTTPException(status_code=503, detail="Something's gone terribly wrong, try again later")