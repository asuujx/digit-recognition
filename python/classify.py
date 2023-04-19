import pandas as pd
import numpy as np
import random as rd
import pathlib
# from PIL import Image

digit_data = pd.read_csv(pathlib.Path(
    __file__).parent.joinpath("mnist_train.csv").absolute())
# Limit amount of each digit
limit = 50
digit_data_0 = digit_data[digit_data["label"] == 0][:limit]
digit_data_1 = digit_data[digit_data["label"] == 1][:limit]
digit_data_2 = digit_data[digit_data["label"] == 2][:limit]
digit_data_3 = digit_data[digit_data["label"] == 3][:limit]
digit_data_4 = digit_data[digit_data["label"] == 4][:limit]
digit_data_5 = digit_data[digit_data["label"] == 5][:limit]
digit_data_6 = digit_data[digit_data["label"] == 6][:limit]
digit_data_7 = digit_data[digit_data["label"] == 7][:limit]
digit_data_8 = digit_data[digit_data["label"] == 8][:limit]
digit_data_9 = digit_data[digit_data["label"] == 9][:limit]
# Make pandas dataframe
short_digit_data = pd.concat([digit_data_0, digit_data_1, digit_data_2, digit_data_3,
                              digit_data_4, digit_data_5, digit_data_6, digit_data_7,
                              digit_data_8, digit_data_9])


# 0 - 255
max_val = digit_data.drop(columns="label").max().max()
half_val = max_val / 2


# List of all pixels
X = digit_data.columns[1:].to_list()
# List of all digits
Y = sorted(list(digit_data["label"].unique()))


class ProcessData:
    @staticmethod
    def normalize(frame):
        frame_c = frame.copy()
        n = len(frame_c)
        for x in X:
            for i in range(n):
                val = frame_c.iloc[i].loc[x]
                frame_c.iloc[i].loc[x] = 1 if val >= half_val else 0
        return frame_c


class FuzzySet:
    @staticmethod
    def calc_hamming(x, y):
        d = 0
        for pixel in X:
            a = x[pixel]
            b = y[pixel]
            d += a*(1-b) + b*(1-a)
#         print(d)
        return d

    def classify(train_set, sample):
        train_set_c = train_set.copy()
        n = len(train_set_c.index)
        dists = []
        for i in range(n):
            dists.append(FuzzySet.calc_hamming(sample, train_set_c.iloc[i]))
        train_set_c["distance"] = dists
        train_set_c.sort_values("distance", inplace=True)
#         print(train_set_c)
        closests = train_set_c[["label", "distance"]][:10]
        return train_set_c.iloc[0]["label"], closests


# class DigitImage:
#     @staticmethod
#     def convert(frame_row):
#         return np.array(frame_row[1:]).reshape(28, 28).astype(int)

#     @staticmethod
#     def get(frame_row):
#         pixels = DigitImage.convert(frame_row)
#         img = Image.fromarray(pixels).convert("1")


def main():
    sample_frame = pd.read_json(pathlib.Path(
        __file__).parent.joinpath("digit.json").absolute())

    normalized_digit_data = ProcessData.normalize(short_digit_data)
    normalized_sample_frame = ProcessData.normalize(sample_frame)

    # sample_original = sample_frame.iloc[0]
    sample = normalized_sample_frame.iloc[0]
    result, closests = FuzzySet.classify(normalized_digit_data, sample)

    print(result)


main()
