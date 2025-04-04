def suma_3_cifre(lista_numere):
    numere_cerute = []
    for numar in lista_numere:
        ultima_cifra = numar % 10
        if (numar / 100) > 1 and numar == ultima_cifra:
            numere_cerute.append(numar)
    print (numere_cerute)


    return 0

print(suma_3_cifre([505, 600, 22, 6006, 101]))