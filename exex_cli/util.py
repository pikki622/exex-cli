def array_dimensions(arr):
    x = 0
    y = 0

    if isinstance(arr, list):
        x = len(arr)

        if arr and isinstance(arr[0], list):
            y = len(arr[0])

    return x, y
