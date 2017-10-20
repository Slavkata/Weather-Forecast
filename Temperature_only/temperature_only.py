import pandas as p
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from XTransformer import XTransformer
from RoundTransformer import RoundTransformer as rt

np.set_printoptions(threshold = sys.maxsize)

def getData(path):
    file = open(path, 'rb')
    return p.read_csv(file)

def getY(data):
    data = data.rename(columns = {'T' : 'Tm'})
    return data [['Tm']].as_matrix()

X_path = './trainData.csv'
y = getY(getData('./trainData.csv'))
X = getData(X_path)

pl = make_pipeline(Ridge(alpha = 2, fit_intercept = True))

X = XTransformer().transform(getData(X_path))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

pl.fit(X_train, y_train)

y_pred = pl.predict(X_test)
y_pred = rt().transform(y_pred[0][0])

print (pl.score(X_test, y_test))
