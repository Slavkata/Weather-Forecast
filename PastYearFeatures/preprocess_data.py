import numpy as np
import pandas as p

class PreprocessData():
    def __init__(self, name):
        self.file_name = file_name

    def get_date_time_t(self, file_name):
        data = p.read_csv(file_name)
        data [['Date', 'Time']] = data.DateAndTime.str.split(expand = True)
        data.Date = self.removeYear(data)
        return data[['Date', 'Time', 'T']]

    def preprocess(training_flag):
        data = self.get_date_time_t(self.file_name)
        data_date = p.get_dummies(data.Date.to_frame())
        data_time = p.get_dummies(data.Time.to_frame())
        data_target = dicty[['T']];

        if training_flag:
            temp_data = data.Date.to_frame().apply(lambda x: p.Series(training(x, data_target)), axis=1)
        else:
            temp_data = data.Date.to_frame().apply(lambda x: p.Series(predicting(x, data_target)), axis=1)

        result = p.concat([data_date, data_time, temp_data], axis=1)
        result.iloc[:len(result.index) - 365].to_csv("features.csv")
        data_target.iloc[:len(data_target.index) - 365].to_csv("target.csv")

        if training_flag:
            return "features.csv", "target.csv"
        else:
            return "features.csv"

    def removeYear(data):
        data [['Day', 'Month', 'Year']] = data.Date.str.split(pat = '.', expand = True)
        data.loc[:, 'Date'] = data[['Day', 'Month']].apply(lambda x: '.'.join(x), axis = 1)
        return data.Date

    def application(row, temperature_data):
        after_drop = temperature_data.drop([row.name])

        if row.name + 365 <= len(after_drop.index):
            return after_drop.iloc[range(row.name, row.name + 365)].T.as_matrix()[0]
        return None

    def application(row, temperature_data):
        if row.name + 365 <= len(temperature_data.index):
            return temperature_data.iloc[range(row.name, row.name + 365)].T.as_matrix()[0]
        return None
