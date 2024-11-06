# 1. Lista de cuvinte și alegerea cuvântului la întâmplare

import random
from operator import index

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print ("Ghiceste cuvantul: " + str(progres) + "\n")

while incercari_ramase != 0 and progres.count("_") != 0:
    incercare = str(input("Ghiceste litera: "))
    if len(incercare) != 1:
        print("\nConditie nerespectata!\n")

    if incercare in progres:
        print("\nLitera se regaseste deja in secventa!\n")
        incercari_ramase -= 1
        print (progres)
        print(f"\nMai ai {incercari_ramase}" + " incercari\n")
        continue

    if incercare not in cuvant_de_ghicit:
        print ("Mai incearca!\n")
        litere_incercate.append(incercare)
        incercari_ramase -=1
        print (progres)
        print(f"\nMai ai {incercari_ramase}" + " incercari\n")
        continue

    if incercare in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if incercare == cuvant_de_ghicit[i]:
                progres[i] = incercare
        print(progres)

if incercari_ramase == 0:
    print(f"Ai piredut! Cuvantul era: {cuvant_de_ghicit}\n")
else:
    print(f"Ai castigat, cuvantul era : {cuvant_de_ghicit} si ti-au mai ramas {incercari_ramase}.!\n")


