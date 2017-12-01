import numpy as np
import pandas as p

data = p.read_csv("3yearsData.csv")

def removeYear(data):
    data [['Day', 'Month', 'Year']] = data.Date.str.split(pat = '.', expand = True)
    data.loc[:, 'Date'] = data[['Day', 'Month']].apply(lambda x: '.'.join(x), axis = 1)
    return data.Date

data [['Date', 'Time']] = data.DateAndTime.str.split(expand = True)
data.Date = removeYear(data)
# data = data.drop_duplicates(subset='Date')
dicty = data[['Date', 'T']]

data_date = p.get_dummies(dicty.Date.to_frame())
temperature_data = dicty[['T']];

def process(row):
    print(row)
    return np.append(row, temperature_data.drop([row.name]))

temp_data = dicty.Date.to_frame().apply(lambda x: p.Series(process(x)), axis=1)

temp_data.to_csv("a.csv")
result = p.concat([data_date, temp_data], axis=1)
result.to_csv("ppdData.csv")
temperature_data.to_csv("target.csv")
