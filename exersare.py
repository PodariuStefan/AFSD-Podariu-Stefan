def max_sir(lista):
    numar_caractere = []
    aparitie_unica = True
    for element in lista:
        numar_caractere.append(len(element))

    for element in lista:
        if lista.count(element) != 1:
            aparitie_unica = False

    majorant = max(numar_caractere)
    i = numar_caractere.index(majorant)
    cuantor = count()

    if aparitie_unica:
        cuantor = 1
        print(f"Cel mai lung șir este \"{lista[i]}\" și apare de {cuantor} ori.")
    else:
        print(f"Cel mai lung șir este \"{lista[i]}\" și apare de {lista[i].count()} ori.")
