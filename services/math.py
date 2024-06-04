import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

def generate_pvalues(x_vals, y_vals):
    '''generates pvalues for the independent variables passed as x_vals'''
    
    est = sm.OLS(y_vals, x_vals).fit()
    
    return est.pvalues