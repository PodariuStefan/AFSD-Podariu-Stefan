import customtkinter as ctk

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

    student = f"{nume} - Nota: {nota}"
    catalog.append(student)
    actualizeaza_lista()
    label_status.configure(text="Student adăugat!")

    entry_nume.delete(0, "end")
    entry_nota.delete(0, "end")

# Funcție pentru ștergerea unui student
def sterge_student():
    global student_selectat
    
    if student_selectat is None:
        label_status.configure(text="Selectează un student din listă!")
        return
    
    try:
        # Găsește indexul studentului în catalog
        index = catalog.index(student_selectat)
        
        # Șterge din catalog
        catalog.pop(index)
        
        # Actualizează lista din interfață
        actualizeaza_lista()
        
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
    
    try:
        numar = int(entry_selectie.get())
        if 1 <= numar <= len(catalog):
            student_selectat = catalog[numar - 1]
            label_status.configure(text=f"Selectat: {student_selectat}")
            entry_selectie.delete(0, "end")
        else:
            label_status.configure(text=f"Introdu un număr între 1 și {len(catalog)}!")
    except ValueError:
        label_status.configure(text="Introdu un număr valid!")

# Funcție pentru selectarea unui student din listă
def selecteaza_student(event):
    global student_selectat
    
    try:
        # Obține poziția mouse-ului în textbox
        cursor_pos = lista.index(f"@{event.x},{event.y}")
        line_num = int(cursor_pos.split(".")[0])
        
        # Indexul în lista catalog (liniile încep de la 1 în tkinter)
        line_index = line_num - 1
        
        if 0 <= line_index < len(catalog):
            student_selectat = catalog[line_index]
            label_status.configure(text=f"Selectat: {student_selectat}")
            entry_selectie.delete(0, "end")
            entry_selectie.insert(0, str(line_index + 1))
        else:
            student_selectat = None
            label_status.configure(text="")
    except (ValueError, IndexError, Exception):
        # Dacă nu se poate determina linia, resetează selecția
        student_selectat = None
        label_status.configure(text="")

# Elemente UI
entry_nume = ctk.CTkEntry(root, placeholder_text="Nume student")
entry_nume.pack(pady=10)

entry_nota = ctk.CTkEntry(root, placeholder_text="Nota")
entry_nota.pack(pady=10)

buton_adauga = ctk.CTkButton(root, text="Adaugă Student", command=adauga_student)
buton_adauga.pack(pady=10)

# Secțiune pentru selecția și ștergerea studentului
frame_selectie = ctk.CTkFrame(root)
frame_selectie.pack(pady=10)

label_selectie = ctk.CTkLabel(frame_selectie, text="Selectează studentul (nr.):")
label_selectie.pack(side="left", padx=5)

entry_selectie = ctk.CTkEntry(frame_selectie, placeholder_text="Nr.", width=50)
entry_selectie.pack(side="left", padx=5)

buton_selecteaza = ctk.CTkButton(frame_selectie, text="Selectează", command=selecteaza_prin_numar, width=100)
buton_selecteaza.pack(side="left", padx=5)

buton_sterge = ctk.CTkButton(root, text="Șterge Student", command=sterge_student)
buton_sterge.pack(pady=10)

lista = ctk.CTkTextbox(root, height=200, width=400)
lista.pack(pady=10)
lista.configure(state="normal")

label_status = ctk.CTkLabel(root, text="")
label_status.pack(pady=5)

# Leagă evenimentul de click pe listă de funcția de selecție student
lista.bind("<Button-1>", selecteaza_student)

# Pornește aplicația
root.mainloop()
