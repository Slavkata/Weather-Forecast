from sklearn.base import TransformerMixin, BaseEstimator
import pandas as p

class RoundTransformer(TransformerMixin, BaseEstimator):
    def __init__ (self):
        pass

    def transform(self, y):
        pred = p.Series(y)
        pred = pred.apply(lambda entry: float("{0:.1f}".format(entry)))
        return pred

    def fit(self):
        return self
