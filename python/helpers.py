def get_last_limit(directory):
    try:
        with open(directory.joinpath("lastlimit.txt"), "r") as file:
            return int(file.readline())
    except IOError as err:
        return None


def set_last_limit(directory, limit):
    try:
        with open(directory.joinpath("lastlimit.txt"), "w") as file:
            file.write(str(limit))
    except IOError as err:
        return None
