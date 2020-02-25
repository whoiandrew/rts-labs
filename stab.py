def stabylizer(arr):
    kf = 1/max(arr)
    return list(map(lambda item: item * kf, arr))