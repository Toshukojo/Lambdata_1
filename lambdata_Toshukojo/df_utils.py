'''
utility functions for working with DataFrames
'''

import pandas 
import numpy

TEST_DF = pandas.DataFrame([1,2,3])
Nulls = pandas.DataFrame(pd.isna(TEST_DF))
