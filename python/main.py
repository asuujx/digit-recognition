from fastapi import FastAPI
from pathlib import Path
from load_data import load_sample, load_train_set
from process_data import ProcessData
from fuzzy_set import FuzzySet
from helpers import check_files, get_last_limit, set_last_limit

app = FastAPI()
directory = Path(__name__).parent
shared_path = Path("/shared")
mnist_train_file = shared_path.joinpath("mnist_train.csv")
mnist_train_norm_file = directory.joinpath("mnist_train_norm.csv")


@app.get("/classify/")
async def classify(limit: int = 100):
    print(limit)

    try:
        check_files()
    except FileNotFoundError as err:
        print(err)
        return {"status": "Error", "digit": None, "message": err}

    last_limit = get_last_limit()

    if limit == last_limit and mnist_train_norm_file.is_file():
        train_set_norm = load_train_set(mnist_train_norm_file.absolute())
        X = train_set_norm.columns[1:].to_list()
    else:
        train_set = load_train_set(mnist_train_file.absolute(), limit)
        X = train_set.columns[1:].to_list()
        train_set_norm = ProcessData.normalize(train_set, X)
        # Save normalized train set to another file
        train_set_norm.to_csv(directory.joinpath("mnist_train_norm.csv"), index=False)
        # Save new limit
        set_last_limit(limit)

    sample_set = load_sample()
    sample_norm = ProcessData.normalize(sample_set, X)
    sample = sample_norm.iloc[0]

    result, closests = FuzzySet.classify(train_set_norm, sample, X)

    return {"status": "OK", "digit": result, "message": None}
