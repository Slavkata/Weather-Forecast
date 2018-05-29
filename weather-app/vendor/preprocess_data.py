import numpy as np
import pandas as p
from datetime import datetime, timedelta

class PreprocessData():
    def __init__(self, file_name):
        self.file_name = file_name

    def get_features(self, file_name):
        data = p.read_csv(file_name, skiprows=7, sep=';', header=None)
        data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
        data.columns = ['DateAndTime', 'T', 'Po', 'P', 'Pa', 'U', 'DD', 'Ff', 'ff10',
            'ff3', 'N', 'WW', 'W1', 'W2', 'Tn', 'Tx', 'Cl', 'Nh', 'H', 'Cm', 'Ch',
            'VV', 'Td', 'RRR', 'tR', 'E', 'Tg', 'E\'', 'sss']

        data [['Date', 'Time']] = data.DateAndTime.str.split(expand = True)
        data.Date = self.removeYear(data)
        return data[['Date', 'Time', 'T', 'Po', 'P', 'Pa', 'DD', 'Ff', 'N', 'Tn', 'Tx', 'VV', 'Td']]

    def preprocess(self, training_flag, predict_date):
        data = self.get_features(self.file_name)
        data_date = p.get_dummies(data.Date.to_frame())
        data_time = p.get_dummies(data.Time.to_frame())
        wind_direction = p.get_dummies(data.DD.to_frame())
        cloud_rate = p.get_dummies(data.N.to_frame())

        data_target = data[['T']];

        if training_flag:
            temp_data = data.Date.to_frame().apply(lambda x: p.Series(self.training(x, data_target)), axis=1)
            result = p.concat([data_date, data_time, wind_direction, cloud_rate, temp_data], axis=1)
            result.iloc[:len(result.index) - 365*8].to_csv("./vendor/features.csv")
            data_target.iloc[:len(data_target.index) - 365*8].to_csv("./vendor/target.csv")
            return "./vendor/features.csv", "./vendor/target.csv"

        else:
            temp_data = data.Date.to_frame().apply(lambda x: p.Series(self.predicting(x, data_target)), axis=1)
            data_date = data_date.iloc[:8]

            predict_date = datetime.strptime(predict_date, "%d.%m.%Y")
            new_date_string = ("Date_%02d.%02d") % (predict_date.day, predict_date.month)
            predict_date = predict_date - timedelta(days=1)
            date_string = ("Date_%02d.%02d") % (predict_date.day, predict_date.month)
            data_date[date_string] = 0
            data_date[new_date_string] = 1

            #make it so we exclude time that has a 0 and is the same date as date_string

            result = p.concat([data_date, data_time, wind_direction, cloud_rate, temp_data], axis=1)
            result.iloc[:8].to_csv("./vendor/test_f.csv")
            return "./vendor/test_f.csv"

    def removeYear(self, data):
        data [['Day', 'Month', 'Year']] = data.Date.str.split(pat = '.', expand = True)
        data.loc[:, 'Date'] = data[['Day', 'Month']].apply(lambda x: '.'.join(x), axis = 1)
        return data.Date

    def training(self, row, temperature_data):
        after_drop = temperature_data.drop([row.name])
        if row.name + 365*8 <= len(after_drop.index):
            result = []
            count = 0

            for i in range(365):
                count += 1
                result = np.append(result, after_drop.iloc[row.name + i*8])
                count = 0 if count == 8 else count

            return result
        return None

    def predicting(self, row, temperature_data):
        if row.name < 8:
            result = []
            count = 0

            for i in range(365):
                count += 1
                result = np.append(result, temperature_data.iloc[i*8])
                count = 0 if count == 8 else count

            return result
        return None
