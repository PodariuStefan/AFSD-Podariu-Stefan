import tkinter as tk
from ctypes.wintypes import LANGID
from tkinter import *
from tkinter import ttk
import random
#from Proiect.environmental_variables import *

def column_generator(nums):
    random_numbers = []
    for i in range(nums):
        random_numbers.append(random.randint(10, 200))

    c_height = 400
    c_width = 512
    x_width = c_width / (len(nums) + 1)
    offset = 30

    for i in enumerate(random_numbers):
        x0 = (i * x_width) + offset
        y0 = c_height - height
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(nums[i]))

def generation():
    print(column_generator())

# Setting the container which will hold everything
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("1024x800")
root.config(bg="#353535")
# Frame that will contain ONLY the canvas
topframe = ttk.Frame(root, height=400, width=800)
#topframe.columnconfigure(0, weight=1)
#topframe.rowconfigure(0, weight=1)
topframe.grid(row= 0, column= 0, sticky= (W, E))
canvas = tk.Canvas(topframe, height=400, width= 512)
canvas.columnconfigure(0, weight=1)
canvas.rowconfigure(0, weight=1)
canvas.grid()
num_of_columns = 8


#rectangle_GUI = canvas.create_rectangle(0, 100, width=2, fill = "white")

#Frame used for different buttons
options_frame = Button(root, text="generate", command=generation)
options_frame.grid(row= 0, column= 1, padx= 10, pady = 5)
#options_frame.grid(row=0, column=1)
#root.grid_rowconfigure(0, weight=0)
#root.grid_columnconfigure(1, weight=1)

#Cool label
#prog_title= Label(options_frame, text="Sorting Algorithm Visualizer")
#prog_title.grid(row=0, column=1, sticky="N")

#Random column generator button
#randomize_col = Button(options_frame, text="Randomize")
#randomize_col.grid(row = 1, column= 0)

root.mainloop()