from tkinter import *
from tkinter import ttk
import random

def drawData(data):
    c_height= 300
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30

    for i, height in enumerate(data):
        x0 = i * x_width + offset
        y0 = c_height - height
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

def generation():
    print("Algorithm Selected: " + selected_alg.get())
    print(drawData([1,2,4,7,5,18,50,32]))
root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900, 600)
root.config(bg="black")

#Variables
selected_alg= StringVar()

#Frame/Base Layout
UI_frame = Frame(root, width=600, height=200, bg="grey")
UI_frame.grid(row=0 , column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=300, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

#Row[0]
Label(UI_frame, text="Algorithm: ", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
alg_menu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=["Bubble Sort", "Merge Sort"])
alg_menu.grid(row=0, column=1, padx=5, pady=5)
alg_menu.current(0)
Button(UI_frame, text="Generate", command=generation, bg="red").grid(row=0, column=2, padx=5, pady=5)

#Row[1]
Label(UI_frame, text="Size: ", bg="grey").grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="MinValue: ", bg="grey").grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="MaxValue: ", bg="grey").grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

root.mainloop()