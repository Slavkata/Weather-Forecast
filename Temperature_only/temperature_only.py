import pandas as p
import sys
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from XTransformer import XTransformer
from sklearn.model_selection import GridSearchCV

np.set_printoptions(threshold = sys.maxsize)

def getData(path):
    file = open(path, 'rb')
    return p.read_csv(file)

def getY(data):
    data = data.rename(columns = {'T' : 'Tm'})
    return data [['Tm']].as_matrix()

X_path = './tData.csv'
y = getY(getData('./tData.csv'))
X = getData(X_path)

params = {
    'ridge__alpha': (0.00001, 0.000001),
}

pipeline = Pipeline([
    ('xtrans', XTransformer()),
    ('ridge', Ridge())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

grid_search = GridSearchCV(pipeline, params, n_jobs = -1, verbose = 1)

grid_search.fit(X_train, y_train)

import subprocess as sp
sp.call('clear', shell=True)

print (grid_search.best_score_)
print (grid_search.best_estimator_)
