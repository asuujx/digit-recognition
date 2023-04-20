from sys import argv
from load_data import load_data
from process_data import ProcessData
from fuzzy_set import FuzzySet
from helpers import get_last_limit, set_last_limit
from pathlib import Path

directory = Path(__file__).parent


def main():
    limit = int(argv[1])

    # If train set limit is equal do not normalize same dataset again
    last_limit = get_last_limit(directory)
    if limit != last_limit:
        train_set, sample_set = load_data(limit)
        X = train_set.columns[1:].to_list()
        train_set_norm = ProcessData.normalize(train_set, X)
        # Save normalized train set to another file
        train_set_norm.to_csv(directory.joinpath(
            "mnist_train_norm.csv"), index=False)
        # Save new limit
        set_last_limit(directory, limit)
    else:
        train_set_norm, sample_set = load_data(
            train_set_file_name="mnist_train_norm.csv")
        X = train_set_norm.columns[1:].to_list()

    sample_norm = ProcessData.normalize(sample_set, X)

    sample = sample_norm.iloc[0]
    result, closests = FuzzySet.classify(train_set_norm, sample, X)

    print(result)


# if __name__ == "main":
main()
