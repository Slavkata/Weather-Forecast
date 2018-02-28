import pandas as p
import numpy as np
from sklearn.linear_model import Ridge
import sys
from sklearn.externals import joblib
from preprocess_data import PreprocessData as pd
from model_export import ModelExport as me
from file_setup_helper import FileSetupHelper as fsh

def main():
    file_name = fsh(sys.argv[1], 366, 1).download_csv()

    features_file_name = pd(file_name).preprocess(False, sys.argv[1])

    X_predict = p.read_csv(features_file_name).drop(['Unnamed: 0'], axis=1)

    predictor = joblib.load(sys.argv[2] + '.plk')

    p.DataFrame((predictor.predict(X_predict))).to_csv("./vendor/predi.csv")

if __name__ == "__main__":
    main()
