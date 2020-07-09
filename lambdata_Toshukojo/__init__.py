'''
lambdata - a collection of data science helper functions
'''
import pandas as pd
import numpy as np
 
#sample codea-
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

def Nulls(x):
    '''
    Reports the total number of null values in a column
    '''
    print('Total Null Values:', x.isnull().sum())
    return

def enlarge(n):
    ''' This function will multiply the input by 100'''
    return n * 100

 
def list_to_series(List):
    '''
    Single function to take a list, turn it into a series and add it to a
    dataframe as a new column
    '''
    pd.DataFrame(List)
    