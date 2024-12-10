def reverse_string(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end="")

reverse_string("onomatopee")

def rangee(start =0, end, step = 1):
    range_list = []
    while start <= end:
        range_list.append(start)
        start += step
    return range_list

rangee(6)