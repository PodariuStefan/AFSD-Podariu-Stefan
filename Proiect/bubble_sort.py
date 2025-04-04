def sort(arr):
    for index in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break