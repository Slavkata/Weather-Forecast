import pandas as p
import numpy as np
from sklearn.linear_model import Ridge
import sys
from sklearn.externals import joblib
from preprocess_data import PreprocessData as pd
from model_export import ModelExport as me
from file_setup_helper import FileSetupHelper as fsh

def main():
    #call for file download with given date
    file_name = fsh(sys.argv[1], 366, 1).download_csv()

    #aquire filename for the features dataset
    features_file_name = pd(file_name).preprocess(False, sys.argv[1])

    #read data from the file
    X_predict = p.read_csv(features_file_name).drop(['Unnamed: 0'], axis=1)

    #load previously exported model
    predictor = joblib.load(sys.argv[2] + '.plk')

    #predict and export prediction to csv
    p.DataFrame((predictor.predict(X_predict))).to_csv("predi.csv")

if __name__ == "__main__":
    main()
