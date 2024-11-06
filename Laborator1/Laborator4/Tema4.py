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
        print("Conditie nerespectata!")
        continue
    for i in range(0, len(cuvant_de_ghicit)):
        if incercare == i:
            progres[i] = incercare
            print(progres)



