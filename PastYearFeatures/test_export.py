from sklearn.externals import joblib
import pandas as p
from sklearn.model_selection import train_test_split

X = p.read_csv('ppdData.csv').drop(['Unnamed: 0'], axis=1)
y = p.read_csv('target.csv').drop(['Unnamed: 0'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 42)

est = joblib.load('past_year_features_export.plk')

# est.predict(X_test)
print(est.score(X_test, y_test))
