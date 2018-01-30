from sklearn.base import TransformerMixin
from sklearn.base import BaseEstimator
import pandas as p

class XTransformer(TransformerMixin, BaseEstimator):
    def __init__(self):
        pass

    #function removing the year part of the data
    def removeYear(self, data):
        data [['Day', 'Month', 'Year']] = data.Date.str.split(pat = '.', expand = True)
        data.loc[:, 'Date'] = data[['Day', 'Month']].apply(lambda x: '.'.join(x), axis = 1)
        return data.Date

    #transform date and time features to one-hot
    def transform(self, X):
        #selecting Date and time columns
        X [['Date', 'Time']] = X.DateAndTime.str.split(expand = True)
        X.loc[:, 'Date'] = self.removeYear(X)

        #ont-hot encoding representation of Data and time
        date = p.get_dummies(X.Date)
        time = p.get_dummies(X.Time)

        return p.concat([date, time], axis = 1)

    def fit(self, *_):
        return self
