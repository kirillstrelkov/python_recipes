from collections import Counter


def get_duplicates(a):
    return [v for v, c in Counter(a).items() if c > 1]


def flatten(a):
    pass
    # TODO: implement
