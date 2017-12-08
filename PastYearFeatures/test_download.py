from one_date_predictor import OneDatePredictor
import datetime
t = datetime.datetime(2017, 12, 6, 0, 0)

odp = OneDatePredictor(t).download_csv()
print(odp)
