import tkinter as tk
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(algorithm_0.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = tk.Tk()
root.title("Feet to Meters converter")
root.iconbitmap("Troll Face.ico")
root.geometry("250x80")


mainframe = ttk.Frame(root, padding= "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky=(N, W, E, S))
root.columnconfigure(0, weight= 1)
root.rowconfigure(0, weight=1)

algorithm_0 = StringVar()
algorithm_0_entry = ttk.Entry(mainframe, width= 7, textvariable= algorithm_0)
algorithm_0_entry.grid(column=2, row=1, sticky=(W, E))
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky= (W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column= 3, row=3, sticky=W)
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

root.mainloop()