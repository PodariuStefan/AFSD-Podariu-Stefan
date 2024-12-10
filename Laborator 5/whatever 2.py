def gaseste_cnp(lst, data):
    for i in range(0, len(lst)):
        if lst[i][1:7] == data:
            print(f"Primul CNP găsit pentru data de naștere {data} este {lst[i]}.")
            return 0
    print(f"Nu s-a găsit niciun CNP pentru data de naștere {data}.")
    return -1
