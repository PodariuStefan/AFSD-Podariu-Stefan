def read_data():
    with open("elevi.json", 'r') as lista_elevi:
        data = lista_elevi.read()
        lista_elevi.close()
    return data