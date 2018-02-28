import pandas as p
import sys
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from XTransformer import XTransformer
from sklearn.model_selection import GridSearchCV

np.set_printoptions(threshold = sys.maxsize)

#get data from file
def getData(path):
    file = open(path, 'rb')
    return p.read_csv(file)

#extract Y from data
def getY(data):
    data = data.rename(columns = {'T' : 'Tm'})
    return data [['Tm']].as_matrix()

X_path = './tData.csv' #weather data
y = getY(getData('./tData.csv')) #set target
X = getData(X_path) #set features

#model params
params = {
    'ridge__alpha': (0.00001, 0.000001),
}

#init pipeline
pipeline = Pipeline([
    ('xtrans', XTransformer()),
    ('ridge', Ridge())
])

#split data to train features, test features, training target, testing target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

#cross-validation with the pipeline
grid_search = GridSearchCV(pipeline, params, n_jobs = -1, verbose = 1)

#fit the grid_search model with the training data
grid_search.fit(X_train, y_train)

#clean the console output
import subprocess as sp
sp.call('clear', shell=True)

#output model information
print (grid_search.best_score_)
print (grid_search.best_estimator_)
