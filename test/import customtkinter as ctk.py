import customtkinter as ctk
import json
import os

# Setări de bază CTk
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Inițializare fereastră principală
root = ctk.CTk()
root.title("Catalog Studenți")
root.geometry("800x700")

# Listă pentru stocarea studenților (acum va fi listă de dicționare)
catalog = []

# Variabilă pentru a ține evidența studentului selectat
student_selectat = None
index_selectat = None

# Fișierul JSON pentru stocare
FISIER_JSON = "catalog_studenti.json"

# Funcții pentru gestionarea JSON
def incarca_din_json():
    global catalog
    if os.path.exists(FISIER_JSON):
        try:
            with open(FISIER_JSON, 'r', encoding='utf-8') as f:
                catalog = json.load(f)
                actualizeaza_lista()
                label_status.configure(text="Datele au fost încărcate din fișier!")
        except Exception as e:
            label_status.configure(text=f"Eroare la încărcarea datelor: {str(e)}")

def salveaza_in_json():
    try:
        with open(FISIER_JSON, 'w', encoding='utf-8') as f:
            json.dump(catalog, f, ensure_ascii=False, indent=2)
        label_status.configure(text="Datele au fost salvate în fișier!")
    except Exception as e:
        label_status.configure(text=f"Eroare la salvarea datelor: {str(e)}")

# Funcție pentru adăugarea unui student
def adauga_student():
    nume = entry_nume.get()
    nota = entry_nota.get()

    if nume.strip() == "" or nota.strip() == "":
        label_status.configure(text="Completează toate câmpurile!")
        return

    try:
        nota_float = float(nota)
        if nota_float < 1 or nota_float > 10:
            raise ValueError
    except ValueError:
        label_status.configure(text="Nota trebuie să fie între 1 și 10.")
        return

    # Creează dicționar pentru student
    student = {"nume": nume, "nota": nota_float}
    catalog.append(student)
    actualizeaza_lista()
    salveaza_in_json()
    label_status.configure(text="Student adăugat și salvat!")

    entry_nume.delete(0, "end")
    entry_nota.delete(0, "end")

# Funcție pentru actualizarea unui student
def actualizeaza_student():
    global student_selectat, index_selectat
    
    if index_selectat is None:
        label_status.configure(text="Selectează un student din listă!")
        return
    
    nume = entry_nume.get()
    nota = entry_nota.get()

    if nume.strip() == "" or nota.strip() == "":
        label_status.configure(text="Completează toate câmpurile pentru actualizare!")
        return

    try:
        nota_float = float(nota)
        if nota_float < 1 or nota_float > 10:
            raise ValueError
    except ValueError:
        label_status.configure(text="Nota trebuie să fie între 1 și 10.")
        return

    # Actualizează studentul în catalog
    catalog[index_selectat] = {"nume": nume, "nota": nota_float}
    actualizeaza_lista()
    salveaza_in_json()
    label_status.configure(text="Student actualizat și salvat!")
    
    # Resetează selecția
    student_selectat = None
    index_selectat = None
    
    entry_nume.delete(0, "end")
    entry_nota.delete(0, "end")

# Funcție pentru ștergerea unui student
def sterge_student():
    global student_selectat, index_selectat
    
    if index_selectat is None:
        label_status.configure(text="Selectează un student din listă!")
        return
    
    try:
        # Șterge din catalog
        catalog.pop(index_selectat)
        
        # Actualizează lista din interfață
        actualizeaza_lista()
        salveaza_in_json()
        
        label_status.configure(text="Student șters și salvat!")
        student_selectat = None
        index_selectat = None
        
    except (IndexError, ValueError):
        label_status.configure(text="Eroare la ștergerea studentului!")

# Funcție pentru actualizarea listei în interfață
def actualizeaza_lista():
    lista.configure(state="normal")
    lista.delete("1.0", "end")
    for i, student in enumerate(catalog):
        lista.insert("end", f"{i+1}. {student['nume']} - Nota: {student['nota']}\n")
    lista.configure(state="disabled")

# Funcție pentru selectarea unui student prin numărul său
def selecteaza_prin_numar():
    global student_selectat, index_selectat
    
    try:
        numar = int(entry_selectie.get())
        if 1 <= numar <= len(catalog):
            index_selectat = numar - 1
            student_selectat = catalog[index_selectat]
            label_status.configure(text=f"Selectat: {student_selectat['nume']} - Nota: {student_selectat['nota']}")
            # Populează câmpurile pentru editare
            entry_nume.delete(0, "end")
            entry_nota.delete(0, "end")
            entry_nume.insert(0, student_selectat['nume'])
            entry_nota.insert(0, str(student_selectat['nota']))
            entry_selectie.delete(0, "end")
        else:
            label_status.configure(text=f"Introdu un număr între 1 și {len(catalog)}!")
    except ValueError:
        label_status.configure(text="Introdu un număr valid!")

# Funcție pentru selectarea unui student din listă
def selecteaza_student(event):
    global student_selectat, index_selectat
    
    try:
        # Obține poziția mouse-ului în textbox
        cursor_pos = lista.index(f"@{event.x},{event.y}")
        line_num = int(cursor_pos.split(".")[0])
        
        # Indexul în lista catalog (liniile încep de la 1 în tkinter)
        line_index = line_num - 1
        
        if 0 <= line_index < len(catalog):
            index_selectat = line_index
            student_selectat = catalog[line_index]
            label_status.configure(text=f"Selectat: {student_selectat['nume']} - Nota: {student_selectat['nota']}")
            # Populează câmpurile pentru editare
            entry_nume.delete(0, "end")
            entry_nota.delete(0, "end")
            entry_nume.insert(0, student_selectat['nume'])
            entry_nota.insert(0, str(student_selectat['nota']))
            entry_selectie.delete(0, "end")
            entry_selectie.insert(0, str(line_index + 1))
        else:
            student_selectat = None
            index_selectat = None
            label_status.configure(text="")
    except (ValueError, IndexError, Exception):
        # Dacă nu se poate determina linia, resetează selecția
        student_selectat = None
        index_selectat = None
        label_status.configure(text="")

# Frame principal pentru input-uri
frame_input = ctk.CTkFrame(root)
frame_input.pack(pady=20, padx=20, fill="x")

entry_nume = ctk.CTkEntry(frame_input, placeholder_text="Nume student", width=200)
entry_nume.pack(pady=10)

entry_nota = ctk.CTkEntry(frame_input, placeholder_text="Nota", width=200)
entry_nota.pack(pady=10)

# Frame pentru butoane - împărțit în stânga și dreapta
frame_butoane = ctk.CTkFrame(root)
frame_butoane.pack(pady=20, padx=20, fill="x")

# Frame stânga pentru primele 2 butoane - centrat
frame_stanga = ctk.CTkFrame(frame_butoane)
frame_stanga.pack(side="left", fill="both", expand=True, padx=(0, 10))

# Container pentru centrarea butoanelor din stânga
container_stanga = ctk.CTkFrame(frame_stanga, fg_color="transparent")
container_stanga.pack(expand=True)

buton_adauga = ctk.CTkButton(container_stanga, text="Adaugă Student", command=adauga_student)
buton_adauga.pack(pady=10)

buton_actualizeaza = ctk.CTkButton(container_stanga, text="Actualizează Student", command=actualizeaza_student)
buton_actualizeaza.pack(pady=10)

# Frame dreapta pentru restul butoanelor - centrat
frame_dreapta = ctk.CTkFrame(frame_butoane)
frame_dreapta.pack(side="right", fill="both", expand=True, padx=(10, 0))

# Container pentru centrarea elementelor din dreapta
container_dreapta = ctk.CTkFrame(frame_dreapta, fg_color="transparent")
container_dreapta.pack(expand=True)

# Secțiune pentru selecția studentului
frame_selectie = ctk.CTkFrame(container_dreapta)
frame_selectie.pack(pady=10)

label_selectie = ctk.CTkLabel(frame_selectie, text="Selectează studentul (nr.):")
label_selectie.pack(pady=5)

entry_selectie = ctk.CTkEntry(frame_selectie, placeholder_text="Nr.", width=100)
entry_selectie.pack(pady=5)

buton_selecteaza = ctk.CTkButton(frame_selectie, text="Selectează", command=selecteaza_prin_numar, width=120)
buton_selecteaza.pack(pady=5)

buton_sterge = ctk.CTkButton(container_dreapta, text="Șterge Student", command=sterge_student)
buton_sterge.pack(pady=10)

# Textbox fără frame, direct cu pack
lista = ctk.CTkTextbox(root, height=200, width=600)
lista.pack(pady=20, padx=20)
lista.configure(state="normal")

label_status = ctk.CTkLabel(root, text="")
label_status.pack(pady=10)

# Leagă evenimentul de click pe listă de funcția de selecție student
lista.bind("<Button-1>", selecteaza_student)

# Încarcă datele la pornire
incarca_din_json()

# Pornește aplicația
root.mainloop()
