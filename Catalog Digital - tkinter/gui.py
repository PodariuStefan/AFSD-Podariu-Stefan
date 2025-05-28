import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.resizable(False, False)

# CRUD options
options_frm = tk.Frame(root, bg= "red", height=350, width=60)
options_frm.grid(row= 0, column= 1, padx=(20, 35), pady=(20,0), sticky="N, W, E")
option = tk.StringVar()
choice = ttk.Combobox(options_frm, width=10, textvariable=option)
choice["values"] = (
                    " Adaugă"
                    " Sterge"
                    " Modifică"
                    " Șterge"
                    )
choice.current()
if option == "Adaugă":


choice.grid()


# Show menu
show_frm = tk.Frame(root, bg="black", height=400, width=700)
show_frm.grid(row=0, column=0, padx=(10, 15), pady=(10, 0), sticky="S, W, N, E")

# User input field
input_frm = tk.Frame(root, bg="green", height=27, width=450)
input_frm.grid(row= 1, column=0, padx=(5, 20), pady=(20, 20), sticky="S, N")

user_input = tk.Entry(input_frm)



root.mainloop()