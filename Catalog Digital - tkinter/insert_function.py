import json
import tkinter as tk
from tkinter import ttk
from read_function import read_data

def insert_values(user_id, name, grades):
    elev = {
        "id": user_id,
        "nume": f"{name}",
        "note": grades
    }

    return elev

def convert2json(dictionary):
    return json.dumps(dictionary)

def set_id():
    dict_len = len(read_data())
    if dict_len < 1:
        next_id = 0
    elif dict_len == 1:
        next_id = 1
    else:
        next_id = dict_len
        print(dict_len)

    return next_id

def write2file(content):
    with open("elevi.json", 'w') as lista_elevi:
        lista_elevi.write(content)
        lista_elevi.close()

def main():
    id_elev = set_id()
    name = input("Nume: ")
    grade = input("Adaugati nota: ")
    elev = insert_values(id_elev, name, grade)
    result = convert2json(elev)
    write2file(result)

if __name__ == "__main__":
    main()

