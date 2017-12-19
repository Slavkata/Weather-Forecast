import pandas as p
import numpy as np
from file_setup_helper import FileSetupHelper as fsh
from preprocess_data import PreprocessData as pd
from model_export import ModelExport as me
import sys
from sklearn.linear_model import Ridge

def main():
    file_name = fsh(sys.argv[1], 1460, 0).download_csv()
    features_file_name, target_file_name = pd(file_name).preprocess(True, None)

    model = Ridge(alpha=1, fit_intercept=True)
    X_train = p.read_csv(features_file_name).drop(['Unnamed: 0', 'Date_29.02'], axis=1)
    y_train = p.read_csv(target_file_name).drop(['Unnamed: 0'], axis=1)

    me(model, X_train, y_train).fit_and_export(sys.argv[2])

if __name__ == '__main__':
    main()
