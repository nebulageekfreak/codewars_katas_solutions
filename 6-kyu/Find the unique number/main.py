def find_uniq(arr):
    return next(x for x in set(arr) if arr.count(x) == 1)