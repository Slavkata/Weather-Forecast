import pandas as p
import numpy as np
from sklearn.linear_model import Ridge
import sys
from sklear,.externals import joblib
from preprocess_data import PreprocessData as pd
from model_export import ModelExport as me
from file_setup_helper import FileSetupHelper as fsh

def main():
    file_name = fsh(sys.argv[1]).download_csv()

    features_file_name, target_file_name = pd(file_name).preprocess()

    model = Ridge(alpha=1, fit_intercept=True)
    X_predict = p.read_csv(features_file_name).drop(['Unnamed: 0'], axis=1)
    y_predict = p.read_csv(target_file_name).drop(['Unnamed: 0'], axis=1)

    model_file_name = me(model, X, y).fit_and_export("ridge_export")

    predictor = joblib.load(model_file_name)

    print(predictor.predict())
