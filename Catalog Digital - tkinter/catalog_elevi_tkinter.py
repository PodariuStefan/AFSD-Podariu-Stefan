import customtkinter as ctk
import json

# Initializarea unei variabile cu valorile din json
with open("elevi.json", 'r') as date_elevi:
    toti_elevi = json.load(date_elevi)
    date_elevi.close()

# Functie de cautare a unui elev din json, returneaza un dictionar
def cauta_student(nume_student):
    numar_studenti = len(toti_elevi["elevi"])
    i = 0
    for elev in toti_elevi["elevi"]:
        i += 1
        if elev["nume"] == nume_student and not(i > numar_studenti):
            return toti_elevi["elevi"][i -1]
    return -1

# Functie ce afiseaza elevii initiali la inceputul programului
def afisare_elevi():
    for elev in toti_elevi["elevi"]:
        lista.configure(state="normal")
        lista.delete("0.0", "end")
        inserare_student(elev["nume"], elev["note"])


# Functie care modifica fisierul json
def modfica_json(intrare):
    toti_elevi["elevi"].append(intrare)
    with open("elevi.json", "w+") as fisier_json:
        json.dump(toti_elevi, fisier_json, indent=2, ensure_ascii=False)
        label_status.configure(text="Datele au fost salvate în fișier!")

# Setări de bază CTk
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Inițializare fereastră principală
root = ctk.CTk()
root.title("Catalog Studenți")
root.geometry("700x700")

# Listă pentru stocarea studenților
catalog = []

# Variabilă pentru a ține evidența studentului selectat
student_selectat = None
index_selectat = None

def inserare_student(nume, nota):
    global nume_student
    nume_student = nume
    student = f"{nume} - Note: {nota}"
    catalog.append(student)

    actualizeaza_lista()

# Funcție pentru adăugarea unui student
def adauga_student():
    nume = entry_nume.get()
    note = entry_nota.get()

    try:
        if cauta_student(nume) != -1:
            raise ValueError
    except ValueError:
        label_status.configure(text="Nu pot fi adăugate persoane care se află deja în catalog!")
        return

    if nume.strip() == "" or note.strip() == "":
        label_status.configure(text="Completează toate câmpurile!")
        return


    # variabila care va determina daca try/except block-ul va returna un mesaj de eroare
    numere_invalide = False

    lista_caractere_sterse = [" ", ",", "[", "]"]
    lista_numere = [] # format string
    contor_separator = 0 # verifica daca stringul are separator dupa o singura cifra
                         # daca ajunge la 2 da mesajul de eroare

    for element in range(len(note)):
        if note[element] in lista_caractere_sterse:
            contor_separator = 0
        else:
            lista_numere.append(float(note[element]))
            contor_separator += 1

        if contor_separator == 2:
            numere_invalide = True

    try:
        if numere_invalide:
            raise ValueError
    except ValueError:
        label_status.configure(text="Numerele nu pot fi mai mici de 1 sau mai mari de 10!")
        return

    inserare_student(nume, note)
    modfica_json({"nume": nume, "note": lista_numere})
    label_status.configure(text="Student adăugat!")

    entry_nume.delete(0, "end")
    entry_nota.delete(0, "end")


def actualizeaza_student():
    global student_selectat

    try:
        if not student_selectat:
            raise ValueError
    except ValueError:
        label_status.configure(text="Selectează un student din listă!")
        return

    lista_nume = 0
    for i, student in enumerate(catalog):
        if student.split(" ") == student_selectat.split(" "):
            lista_nume= student.split(" ")
            index_selectat = i
            lista_nume = lista_nume[0:1]

    nume_elev = lista_nume[0]
    lista_note = 0
    for elev in toti_elevi["elevi"]:
        if elev["nume"] == nume_elev:
            lista_note = entry_nota.get()

    if nume_elev.strip() == "" or lista_note == "":
        label_status.configure(text="Completează toate câmpurile pentru actualizare!")
        return

    lista_numere = list(lista_note) # lista de caractere
    lista_numere_prelucrate = []

    for element in lista_numere:
        if element == " ":
            continue
        lista_numere_prelucrate.append(int(element))

    # variabila care va determina daca try/except block-ul va returna un mesaj de eroare
    numere_invalide = False

    for numar in lista_numere_prelucrate:
        if numar > 10 or numar < 1:
            numere_invalide = True
    try:
        if numere_invalide:
            raise ValueError
    except ValueError:
        label_status.configure(text="Numerele nu pot fi mai mici de 1 sau mai mari de 10!")
        return

    # Actualizează studentul în catalog
    catalog[index_selectat] = f"{nume_elev} - Note: {str(lista_numere_prelucrate)}"

    # Modificari parametrii json
    with open("elevi.json", "w+") as file:

        for elev in toti_elevi["elevi"]:
            if elev["nume"] == nume_elev:
                elev["note"] = lista_numere_prelucrate
                elev["nume"] = entry_nume.get()
        label_status.configure(text="Student actualizat și salvat!")
        json.dump(toti_elevi, file, indent=2)

    catalog.clear()
    actualizeaza_lista()

    # Resetează selecția
    student_selectat = None
    index_selectat = None

    entry_nume.delete(0, "end")
    entry_nota.delete(0, "end")

    #Afisare lista noua
    afisare_elevi()

# Funcție pentru ștergerea unui student
def sterge_student():
    global student_selectat
    
    if student_selectat is None:
        label_status.configure(text="Selectează un student din listă!")
        return
    nume_student = student_selectat.split(" ")
    try:
        # Găsește indexul studentului în catalog
        index = catalog.index(student_selectat)

        # Șterge din catalog
        catalog.pop(index)

        # Actualizează lista din interfață
        actualizeaza_lista()

        #print(index)
        #Eliminare date din json
        for elev in toti_elevi["elevi"]:
           if elev["nume"] == nume_student[0]:
                toti_elevi["elevi"].remove(elev)
                break

        with open("elevi.json", "w+") as file:
            json.dump(toti_elevi, file, indent=2)
            file.close()

        label_status.configure(text="Student șters!")
        student_selectat = None
        
    except ValueError:
        label_status.configure(text="Eroare la ștergerea studentului!")

# Funcție pentru actualizarea listei în interfață
def actualizeaza_lista():
    lista.configure(state="normal")
    lista.delete("1.0", "end")
    for i, student in enumerate(catalog):
        lista.insert("end", f"{i+1}. {student}\n")
    lista.configure(state="disabled")

# Funcție pentru selectarea unui student prin numărul său
def selecteaza_prin_numar():
    global student_selectat

    numar = int(entry_selectie.get())
    rand_elev = numar - 1
    atributii_elev = toti_elevi["elevi"][rand_elev]
    nume_elev = atributii_elev.get("nume")
    note_elev = atributii_elev.get("note")

    try:
        if 1 <= numar <= len(catalog):
            student_selectat = catalog[numar - 1]
            label_status.configure(text=f"Selectat: {student_selectat}")
            entry_selectie.delete(0, "end")
            entry_nume.delete(0, "end")
            entry_nota.delete(0, "end")
            entry_nume.insert(0, nume_elev)
            entry_nota.insert(0, note_elev)
        else:
            label_status.configure(text=f"Introdu un număr între 1 și {len(catalog)}!")
    except ValueError:
        label_status.configure(text="Introdu un număr valid!")

# Funcție pentru selectarea unui student din listă
def selecteaza_student(event):
    global student_selectat

    # Obține poziția mouse-ului în textbox
    cursor_pos = lista.index(f"@{event.x},{event.y}")
    line_num = int(cursor_pos.split(".")[0])

    # Indexul în lista catalog (liniile încep de la 1 în tkinter)
    line_index = line_num - 1

    atributii_elev = toti_elevi["elevi"][line_index]
    nume_elev = atributii_elev.get("nume")
    note_elev = atributii_elev.get("note")

    try:
        if 0 <= line_index < len(catalog):
            student_selectat = catalog[line_index]
            label_status.configure(text=f"Selectat: {student_selectat}")
            entry_selectie.delete(0, "end")
            entry_selectie.insert(0, str(line_index + 1))
            entry_nume.delete(0, "end")
            entry_nota.delete(0, "end")
            entry_nume.insert(0, nume_elev)
            entry_nota.insert(0, note_elev)

        else:
            student_selectat = None
            label_status.configure(text="")
    except (ValueError, IndexError, Exception):
        # Dacă nu se poate determina linia, resetează selecția
        student_selectat = None
        label_status.configure(text="")

# Elemente UI

frame_input = ctk.CTkFrame(root)
frame_input.pack(pady=20, padx=20, fill="x")

entry_nume = ctk.CTkEntry(frame_input, placeholder_text="Nume student", width=200)
entry_nume.pack(pady=10)

entry_nota = ctk.CTkEntry(frame_input, placeholder_text="Nota", width=200)
entry_nota.pack(pady=10)

frame_butoane = ctk.CTkFrame(root)
frame_butoane.pack(pady=20, padx=20, fill="x")

frame_stanga = ctk.CTkFrame(frame_butoane)
frame_stanga.pack(side="left", fill="both", expand=True, padx=(0, 10))

frame_dreapta = ctk.CTkFrame(frame_butoane)
frame_dreapta.pack(side="right", fill="both", expand=True, padx=(10, 0))

container_stanga = ctk.CTkFrame(frame_stanga, fg_color="transparent")
container_stanga.pack(expand=True)

buton_adauga = ctk.CTkButton(container_stanga, text="Adaugă Student", command=adauga_student)
buton_adauga.pack(pady=10)

buton_actualizeaza = ctk.CTkButton(container_stanga, text="Actualizează Student", command=actualizeaza_student)
buton_actualizeaza.pack(pady=10)

buton_sterge = ctk.CTkButton(container_stanga, text="Șterge Student", command=sterge_student)
buton_sterge.pack(pady=10)

container_dreapta = ctk.CTkFrame(frame_dreapta, fg_color="transparent")
container_dreapta.pack(expand=True)

label_selectie = ctk.CTkLabel(container_dreapta, text="Selectează studentul (nr.):")
label_selectie.pack(side="left", padx=5)

entry_selectie = ctk.CTkEntry(container_dreapta, placeholder_text="Nr.", width=50)
entry_selectie.pack(side="left", padx=5)

buton_selecteaza = ctk.CTkButton(container_dreapta, text="Selectează", command=selecteaza_prin_numar, width=100)
buton_selecteaza.pack(side="left", padx=5)

lista = ctk.CTkTextbox(root, height=200, width=400)
afisare_elevi()
lista.pack(pady=10)
lista.configure(state="normal")


label_status = ctk.CTkLabel(root, text="")
label_status.pack(pady=5)

# Leagă evenimentul de click pe listă de funcția de selecție student
lista.bind("<Button-1>", selecteaza_student)

# Pornește aplicația
root.mainloop()
