numar_iteratii = 0

def cautare_binara(arr, start, stop, val):
    global numar_iteratii
    while start <= stop:
        numar_iteratii += 1
        mijloc = (start + stop) // 2
        if arr[mijloc] == val:
            return mijloc
        elif arr[mijloc] < val:
            start = mijloc + 1
        else:
            stop = mijloc - 1
    return -1

def cautare_exponentiala(arr, val):
    n = len(arr)
    global numar_iteratii
    numar_iteratii = 0
    if arr[0] == val:
        print(f"Dosarul pacientului cu numărul de identificare {val} a fost găsit la poziția {0} după {0} pași de căutare.")
        return 0
    else:
        i = 1
        while i < n and arr[i] < val:
            numar_iteratii += 1
            i *= 2
        existanta = cautare_binara(arr, i//2, min(i, n-1), val)

        if existanta != -1:
            print(f"Dosarul pacientului cu numărul de identificare {val} a fost găsit la poziția {existanta} după {numar_iteratii} pași de căutare.")
        else:
            print(f"Dosarul pacientului cu numărul de identificare {val} nu a fost găsit. Total pași efectuați: {numar_iteratii}.")

cautare_exponentiala([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1030)

cautare_exponentiala([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1100)

cautare_exponentiala([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1000)

cautare_exponentiala(range(1, 1000000, 7), 7778)

cautare_exponentiala(range(1, 1000000, 7), 1234567)






