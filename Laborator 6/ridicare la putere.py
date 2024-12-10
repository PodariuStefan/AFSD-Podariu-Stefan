def putere(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * putere(a, b -1)



print(putere(11,2))