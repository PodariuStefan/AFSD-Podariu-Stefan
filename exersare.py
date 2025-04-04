def bubblesort(arr):
    for i in range(len(arr) - 1, 0, -1):
        is_sorted = True
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[i], arr[i+1] = arr[i + 1], arr[i]
                is_sorted = False
        if is_sorted:
            break
    return arr

bubblesort([1,2,6,3])