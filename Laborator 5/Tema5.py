from math import sqrt


def cauta_container(containere, numar_identificare):
    numar_pasi = 0
    n = len(containere)
    salt = int(sqrt(n))
    st = 0

    for i in range(0, n, salt):
        numar_pasi += 1
        if containere[i] == numar_identificare:

            print(f"Containerul cu numărul {numar_identificare} a fost găsit pe poziția {i} după {numar_pasi} pași.")
            return i
        elif containere[i] < numar_identificare:
            st = i

            continue
        else:

            break

    for i in range(st, st + salt):
        numar_pasi += 1
        if st + salt < n:

            if containere[i] == numar_identificare:

                print(
                    f"Containerul cu numărul {numar_identificare} a fost găsit pe poziția {i} după {numar_pasi} pași.")
                return i
            elif containere[i] < numar_identificare:

                st = i
                continue
            elif containere[i] + salt < n:

                continue
            else:
                break
        if numar_identificare not in containere:
            numar_pasi = len(containere) - salt
    print(f"Containerul cu numărul {numar_identificare} nu a fost găsit în sistem. Total pași efectuați: {numar_pasi}.")
    return -1

cauta_container([1050, 1075, 1100, 1125, 1150, 1175, 1200], 1300)