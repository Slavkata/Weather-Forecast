import pandas as p
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

np.set_printoptions(threshold = sys.maxsize)
clf = svm.SVR()

def getData(path):
    file = open(path, 'rb')
    return p.read_csv(file)

def getX(data):
    data [['Date', 'Time']] = data.DateAndTime.str.split(expand = True)

    date = p.get_dummies(data.Date)
    time = p.get_dummies(data.Time)

    return p.concat([date, time], axis = 1)

def getY(data):
    data = data.rename(columns = {'T' : 'Tm'})
    return data [['Tm']].as_matrix()

X = getX(getData('./trainData.csv'))
y = getY(getData('./trainData.csv'))
test_data = getX(getData('./testData.csv'))

test_data.to_csv('./test_one_hot.csv')

print(clf.fit(X, y.ravel()).predict([test_data.loc[0]]))
