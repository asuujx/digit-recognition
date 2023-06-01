from pandas import DataFrame, Series


class FuzzySet:
    @staticmethod
    def calc_hamming(x, y, X):
        d = 0
        for pixel in X:
            a = x[pixel]
            b = y[pixel]
            d += a * (1 - b) + b * (1 - a)
        return d

    @staticmethod
    def classify(train_set: DataFrame, sample: Series, X: list):
        train_set_c = train_set.copy()
        n = len(train_set_c.index)
        dists = []
        for i in range(n):
            dists.append(FuzzySet.calc_hamming(sample, train_set_c.iloc[i], X))
        train_set_c["distance"] = dists
        train_set_c.sort_values("distance", inplace=True)
        #         print(train_set_c)
        result = str(train_set_c.iloc[0]["label"])
        closests = train_set_c[["label", "distance"]][:10]
        return result, closests
