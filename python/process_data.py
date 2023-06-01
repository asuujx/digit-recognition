from pandas import DataFrame

class ProcessData:
    @staticmethod
    def normalize(frame: DataFrame, X: list):
        frame_c = frame.copy()
        n = len(frame_c)
        max_val = frame_c.drop(columns="label").max().max()
        half_val = max_val / 2

        for x in X:
            for i in range(n):
                val = frame_c.iloc[i].loc[x]
                frame_c.iloc[i].loc[x] = 1 if val >= half_val else 0
        return frame_c
