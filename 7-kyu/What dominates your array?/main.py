def dominator(arr):
    for x in range(len(arr)):
        if arr.count(arr[x]) > len(arr) - arr.count(arr[x]):
            return arr[x]
    return -1