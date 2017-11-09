import numpy as np
from sklearn.grid_search import GridSearchCV

class GridSearch():

    def __init__(self, X, y, model, params):
        self.X = X
        self.y = y
        self.model = model
        self.params = params

    def runSearch(self):
        clf = GridSearchCV(estimator = self.model, param_grid = self.params, n_jobs = -1)
        clf.fit(self.X, self.y)
        print ('BestScore : ', clf.best_score_)
        print ('Best estimator : ', clf.best_estimator_)
