# This will be a file used to store functions for modeling within the EV Charging Station Individual Project

# -----Imports -----------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

# ----- Functions --------------------------------------------------------------------------------------
# Function to calculate RMSE:
def rmse_evaluation(target_var):
    '''
    This function will take in the actual values in validate and the predicted values
    and compute the mean_squared_error and then take the square root and round to 0 decimals. 
    It will return the RMSE as an integer. 
    '''
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0)
    return rmse


# Function to plot forcasts
def plot_and_eval(target_var):
    '''
    a function to evaluate forecasts by computing the rmse and plot train and validate along with predictions
    '''
    plot_samples(target_var)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(target_var)
    print(target_var, '--RMSE: {:.0f}'.format(rmse))
    plt.show()


# ---------------------
def append_eval_df(eval_df, model_type, target_var):
    '''
    This function will take in the model_type as a string for the name of the model, 
    the target variable as a string, 
    and run the evaluate() function to compute the rmse, 
    and append the dataframe row with the model_type, target_var, and rmse. 
    It will return the new dataframe. 
    '''
    if eval_df.size == 0:
        eval_df = pd.DataFrame(columns = ['model_type', 'target_var', 'rmse'])
        rmse = evaluate(target_var)
        d = {'model_type': [model_type], 'target_var': [target_var], 'rmse': [rmse]}
        d = pd.DataFrame(d)
        return eval_df.append(d, ignore_index=True)
    else:
        rmse = evaluate(target_var)
        d = {'model_type': [model_type], 'target_var': [target_var], 'rmse': [rmse]}
        d = pd.DataFrame(d)
        return eval_df.append(d, ignore_index=True)