import pandas as p
import numpy as np
from file_setup_helper import FileSetupHelper as fsh
from preprocess_data import PreprocessData as pd
from model_export import ModelExport as me
import sys
from sklearn.linear_model import Ridge

def main():
    #call for file download with given date
    file_name = fsh(sys.argv[1], 1460, 0).download_csv()

    #aquire features and target data filenames
    features_file_name, target_file_name = pd(file_name).preprocess(True, None)

    #init model, and open the features and target file
    #(drop column added by pandas and bypass 29.02 potential error)
    model = Ridge(alpha=1, fit_intercept=True)
    X_train = p.read_csv(features_file_name).drop(['Unnamed: 0', 'Date_29.02'], axis=1)
    y_train = p.read_csv(target_file_name).drop(['Unnamed: 0'], axis=1)

    #export model with the given datasets and model
    me(model, X_train, y_train).fit_and_export(sys.argv[2])

if __name__ == '__main__':
    main()
