import pandas as p
import numpy as np
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split


class ModelExport():
    def __init__(self, model, X, y):
        self.model = model
        self.X = X
        self.y = y

    def split_data(self, test_size, random_state):
        return train_test_split(self.X, self.y, test_size = test_size, random_state = random_state)

    def fit_and_export(self, name):
        X_train, X_test, y_train, y_test = self.split_data(0.1, 42)
        self.model.fit(X_train, y_train)
        name += '.plk'
        export = joblib.dump(self.model, name)
        return name
