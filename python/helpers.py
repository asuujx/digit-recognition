from pathlib import Path


directory = Path(__file__).parent
shared_dir = Path("/shared")
sample_file = shared_dir.joinpath("sample.json")
mnist_train_file = shared_dir.joinpath("mnist_train.csv")


def check_files():
    print(shared_dir)
    if not sample_file.is_file():
        raise FileNotFoundError("No sample.json file found in /shared directory")
    if not mnist_train_file.is_file():
        raise FileNotFoundError("No sample.json file found in /shared directory")
    else:
        return True


def get_last_limit():
    try:
        with open(directory.joinpath("lastlimit.txt"), "r") as file:
            return int(file.readline())
    except IOError as err:
        return None


def set_last_limit(limit):
    try:
        with open(directory.joinpath("lastlimit.txt"), "w") as file:
            file.write(str(limit))
    except IOError as err:
        return None
