import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

def generate_pvalues(x_vals, y_vals):
    '''takes dataframe of independent variables and dataframe of dependent variable and returns the pvalues for the OLS regression'''
    
    est = sm.OLS(y_vals, x_vals).fit()
    
    return est.pvalues