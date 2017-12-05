import numpy as np
import pandas as p

def main():
    data = p.read_csv("3yearsData.csv")
    data [['Date', 'Time']] = data.DateAndTime.str.split(expand = True)
    data.Date = removeYear(data)
    dicty = data[['Date', 'Time', 'T']]
    data = None

    data_date = p.get_dummies(dicty.Date.to_frame())
    data_time = p.get_dummies(dicty.Time.to_frame())
    data_temp = dicty[['T']];

    temp_data = dicty.Date.to_frame().apply(lambda x: p.Series(process(x, data_temp)), axis=1)

    result = p.concat([data_date, data_time, temp_data], axis=1)
    result.iloc[:len(result.index) - 365].to_csv("ppdData.csv")
    data_temp.iloc[:len(data_temp.index) - 365].to_csv("target.csv")

def removeYear(data):
    data [['Day', 'Month', 'Year']] = data.Date.str.split(pat = '.', expand = True)
    data.loc[:, 'Date'] = data[['Day', 'Month']].apply(lambda x: '.'.join(x), axis = 1)
    return data.Date

def process(row, temperature_data):
    after_drop = temperature_data.drop([row.name])

    if row.name + 365 <= len(after_drop.index):
        return after_drop.iloc[range(row.name, row.name + 365)].T.as_matrix()[0]
    return None

if __name__ == '__main__':
    main()
