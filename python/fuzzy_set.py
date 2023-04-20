class FuzzySet:
    @staticmethod
    def calc_hamming(x, y, X):
        d = 0
        for pixel in X:
            a = x[pixel]
            b = y[pixel]
            d += a*(1-b) + b*(1-a)
#         print(d)
        return d

    @staticmethod
    def classify(train_set, sample, X):
        train_set_c = train_set.copy()
        n = len(train_set_c.index)
        dists = []
        for i in range(n):
            dists.append(FuzzySet.calc_hamming(sample, train_set_c.iloc[i], X))
        train_set_c["distance"] = dists
        train_set_c.sort_values("distance", inplace=True)
#         print(train_set_c)
        closests = train_set_c[["label", "distance"]][:10]
        return train_set_c.iloc[0]["label"], closests
