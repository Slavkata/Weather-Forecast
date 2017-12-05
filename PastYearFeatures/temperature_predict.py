import pandas as p
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split


X = p.read_csv('ppdData.csv').drop(['Unnamed: 0'], axis=1)
y = p.read_csv('target.csv').drop(['Unnamed: 0'], axis=1)

els = Ridge(alpha = 1, fit_intercept = False)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

els.fit(X_train, y_train)
print(els.score(X_test, y_test))
