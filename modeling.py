# This will be a file used to store functions for modeling within the EV Charging Station Individual Project

# -----Imports -----------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import explained_variance_score
from math import sqrt

# ----- TimeSeries Function(s) ----------------------------------------------------------------------------

# Function to create a dataframe for displaying time series results
def append_eval_df(eval_df, model_type, target_var, actual, predict):
    '''
    This function will take in the model_type as a string for the name of the model, 
    the target variable as a string, 
    and run the evaluate() function to compute the rmse, 
    and append the dataframe row with the model_type, target_var, and rmse. 
    It will return the new dataframe. 
    '''
    if eval_df.size == 0:
        eval_df = pd.DataFrame(columns = ['Model Type', 'Target Variable', 'RMSE'])
        rmse = round(sqrt(mean_squared_error(actual, predict)), 0)
        d = {'Model Type': [model_type], 'Target Variable': [target_var], 'RMSE': [rmse]}
        d = pd.DataFrame(d)
        return eval_df.append(d, ignore_index=True)
    else:
        rmse = round(sqrt(mean_squared_error(actual, predict)), 0)
        d = {'Model Type': [model_type], 'Target Variable': [target_var], 'RMSE': [rmse]}
        d = pd.DataFrame(d)
        return eval_df.append(d, ignore_index=True)



