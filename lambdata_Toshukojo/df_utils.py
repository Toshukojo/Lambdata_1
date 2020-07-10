'''
utility functions for working with DataFrames
'''
import pandas
import numpy
import string
from sklearn.model_selection import train_test_split


TEST_DF = pandas.DataFrame([1, 2, 3])


class dsfunctions(self):
    '''helpful dataframe funtions'''

    def train_validation_test_split(x, y, train_size=0.7, val_size=0.1, test_size=0.2, random_state=None, shuffle=True):
        '''
        takes your split x features and target and splits them into train, validation, and test sets.
        '''

        x_train_val, x_test, y_train_val, y_test = train_test_split(
            x, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

        x_train, x_val. y_train. y_val = train_test_split(
            x_train_val, y_train_val, test_size=val_size/(train_size+val_size),
            random_state=random_state, shuffle=shuffle)

        return x_train, x_val, x_test, y_train, y_val, y_test

    def Nulls(x):
        '''
        Reports the total number of null values in a column
        '''
        print('Total Null Values:', x.isnull().sum())
        return

    def enlarge(n):
        ''' This function will multiply the input by 100'''
        return n * 100

    def increment(x):
        return(x + 1)

    def min_max_scaler(x):
        '''Returns numpy array with original values scaled'''
        return (x - x.min()) / (x.max() - x.min())

    def strip_punctuation(text):
        exclude = string.punctuation
        return ''.join(s for s in text if s not in exclude)

    def bag_of_words(text):
        text = strip_punctuation(text)
        words = set(text.split(' '))
        return words

    def newton_sqrt(n):
        """Return the square root of x using Newton's Method."""
        val = n
        while True:
        last = val
        val = (val + n / val) * 0.5
        if abs(val - last) < 1e-9:
            break
        return val

    def list_to_series(List):
        '''
        Single function to take a list, turn it into a series and add it to a
        dataframe as a new column
        '''
        pd.DataFrame(List)
        pass

