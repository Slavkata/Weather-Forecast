import numpy as np
import pandas as p
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from Estimator import EstimatorSelectionHelper as es
from sklearn.model_selection import train_test_split

X = p.read_csv("ppdData.csv")
y = p.read_csv("target.csv")

pipelines = {
    'Ridge' : Pipeline([ ('ridge', Ridge()) ]),
    'Lasso' : Pipeline([ ('lasso', Lasso()) ]),
    'ElasticNet' : Pipeline([ ('elasticnet', ElasticNet()) ])
}

params = {
    'Ridge' : {
        'ridge__alpha' : (0.0001, 0.001, 0.01, 0.1, 1),
        'ridge__fit_intercept' : (True, False)
    },
    'Lasso' : {
        'lasso__alpha' : (0.0001, 0.001, 0.01, 0.1, 1),
        'lasso__fit_intercept' : (True, False)
    },
    'ElasticNet' : {
        'elasticnet__alpha' : (0.0001, 0.001, 0.01, 0.1, 1),
        'elasticnet__l1_ratio' : (0.1, 0.3, 0.5, 0.7, 0.9, 1),
        'elasticnet__fit_intercept' : (True, False)
    }
}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

estimator = es(pipelines, params)

estimator.fit(X_train, y_train)

print(estimator.score_summary())
estimator.score_summary().to_csv("scores.csv")
