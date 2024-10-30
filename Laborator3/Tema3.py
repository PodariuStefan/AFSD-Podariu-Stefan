from itertools import count
from shutil import which

meniu = ["papanasi"] * 10 + ["ceafa"] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"] # Coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"] # Coada FIFO
tavi = ["tava"] * 7 # Stiva LIFO
istoric_comenzi = []



def cerinta1 ():
    print("Cerința 1: \n")

    for nume in studenti:
        print(nume + " a comandat: " + comenzi[0] + ".")
        tavi.pop()
        istoric_comenzi.extend(comenzi[0:1])
        comenzi.pop(0)

def cerinta2 ():
    print("\nCerința 2: \n")
    print("S-au comnandat: " + str(istoric_comenzi.count("guias")) + " guias" + ", " + str(istoric_comenzi.count("ceafa")) + " cefe" + ", " + str(istoric_comenzi.count("papanasi")) + " papanasi.")
    print("Mai sunt " + str(tavi.count("tava")) + " tavi")
    print("Au mai rămas: " + str(meniu.count("papanasi") - istoric_comenzi.count("papanasi")) + " papanasi, " + str(meniu.count("ceafa") - istoric_comenzi.count("ceafa")) + " cefe, " + str(meniu.count("guias") - istoric_comenzi.count("guias")) + " guiași.")
    if meniu.count("papanasi") - istoric_comenzi.count("papanasi") > 0:
        print ("Au mai ramas papanasi: " + str(any(meniu)))
    else:
        print ("Nu au mai ramas papanasi: " + str(bool(1>2)))
    if meniu.count("ceafa") - istoric_comenzi.count("ceafa") > 0:
        print ("Au mai ramas cefe: " + str(any(meniu)))
    else:
        print ("Au mai ramas cefe: " + str(bool(1>2)))
    if meniu.count("guias") - istoric_comenzi.count("guias") > 0:
        print ("Au mai ramas guiași: " + str(any(meniu)))
    else:
        print ("Au mai ramas guiași: " + str(bool(1>2)))

def cerinta3():
    print("\nCerința 3: \n")
    total = 0
    for profit in preturi:
        if profit [0] in istoric_comenzi:
            total += profit [1]
    print ("Cantina a încasat: " + str(total) + " de lei.")
    for valoare in preturi:
        if valoare [1] >= 7:
            print ("Produsele care costă cel mult 7 lei sunt: " + str(valoare))



def rezolvare ():
    cerinta1()
    cerinta2()
    cerinta3()

rezolvare()

