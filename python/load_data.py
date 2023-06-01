import pandas as pd
from pathlib import Path

pd.options.mode.chained_assignment = None

directory = Path("/shared")
sample_abs_path = directory.joinpath("sample.json").absolute()


def load_sample():
    sample = pd.read_json(sample_abs_path)
    return sample


def load_train_set(abs_path: str, limit: str | None = None):
    train_set = pd.read_csv(abs_path)

    if limit:
        # Limit amount of each digit
        digit_data_0 = train_set[train_set["label"] == 0][:limit]
        digit_data_1 = train_set[train_set["label"] == 1][:limit]
        digit_data_2 = train_set[train_set["label"] == 2][:limit]
        digit_data_3 = train_set[train_set["label"] == 3][:limit]
        digit_data_4 = train_set[train_set["label"] == 4][:limit]
        digit_data_5 = train_set[train_set["label"] == 5][:limit]
        digit_data_6 = train_set[train_set["label"] == 6][:limit]
        digit_data_7 = train_set[train_set["label"] == 7][:limit]
        digit_data_8 = train_set[train_set["label"] == 8][:limit]
        digit_data_9 = train_set[train_set["label"] == 9][:limit]

        # Make pandas dataframe
        train_set_short = pd.concat(
            [
                digit_data_0,
                digit_data_1,
                digit_data_2,
                digit_data_3,
                digit_data_4,
                digit_data_5,
                digit_data_6,
                digit_data_7,
                digit_data_8,
                digit_data_9,
            ]
        )

        return train_set_short
    else:
        return train_set


# def load_data(train_set_file_abs_path: str, limit: int):
#     train_set_full = pd.read_csv(train_set_file_abs_path)
#     sample = pd.read_json(sample_abs_path)

#     if train_set_file_abs_path != "mnist_train.csv":
#         return train_set_full, sample

#     # Limit amount of each digit
#     digit_data_0 = train_set_full[train_set_full["label"] == 0][:limit]
#     digit_data_1 = train_set_full[train_set_full["label"] == 1][:limit]
#     digit_data_2 = train_set_full[train_set_full["label"] == 2][:limit]
#     digit_data_3 = train_set_full[train_set_full["label"] == 3][:limit]
#     digit_data_4 = train_set_full[train_set_full["label"] == 4][:limit]
#     digit_data_5 = train_set_full[train_set_full["label"] == 5][:limit]
#     digit_data_6 = train_set_full[train_set_full["label"] == 6][:limit]
#     digit_data_7 = train_set_full[train_set_full["label"] == 7][:limit]
#     digit_data_8 = train_set_full[train_set_full["label"] == 8][:limit]
#     digit_data_9 = train_set_full[train_set_full["label"] == 9][:limit]

#     # Make pandas dataframe
#     train_set_short = pd.concat(
#         [
#             digit_data_0,
#             digit_data_1,
#             digit_data_2,
#             digit_data_3,
#             digit_data_4,
#             digit_data_5,
#             digit_data_6,
#             digit_data_7,
#             digit_data_8,
#             digit_data_9,
#         ]
#     )

#     return train_set_short, sample
