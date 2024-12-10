import tkinter
from tkinter import *
from bubble_sort import bubble_sort
from tkinter import *

root = tkinter.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("800x600")

label = tkinter.Label(root, text= "Guacamole", font=('Times New Roman', 20))
label.pack(padx = 30, pady = 90)

#textbox = tkinter.Text(root, height= 5, font = ("Aerial", 17))
#textbox.pack(padx = 20, pady =10)

#entry= tkinter.Entry(root)
#entry.pack()

button = tkinter.Button(root, text="Start", font=("Wingdings", 10))
button.pack(pady = 10)


#frame = Frame(root)
#frame.pack()
#
#/bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )
#
#redbutton = Button(frame, text="Red", fg="red")
#redbutton.pack( side = LEFT)
#
#greenbutton = Button(frame, text="Brown", fg="brown")
#greenbutton.pack( side = LEFT )
#
#bluebutton = Button(frame, text="Blue", fg="blue")
#bluebutton.pack( side = LEFT )
#
#blackbutton = Button(bottomframe, text="Black", fg="black")
#blackbutton.pack( side = BOTTOM)
#

frm = tkinter.Frame(root)
frm.columnconfigure(0, weight =1)
frm.columnconfigure(1, weight =1)
frm.columnconfigure(2, weight =1)

btn1 = tkinter.Button(frm, text="1")
btn1.grid(row=0, column= 0, sticky=tkinter.W + tkinter.E)

btn2 = tkinter.Button(frm, text="2")
btn2.grid(row=0, column= 1, sticky=tkinter.W + tkinter.E)

btn3= tkinter.Button(frm, text="3")
btn3.grid(row=0, column= 2, sticky=tkinter.W + tkinter.E)

btn1 = tkinter.Button(frm, text="4")
btn1.grid(row=1, column= 0, sticky=tkinter.W + tkinter.E)

btn1 = tkinter.Button(frm, text="5")
btn1.grid(row=1, column= 1, sticky=tkinter.W + tkinter.E)

btn1 = tkinter.Button(frm, text="6")
btn1.grid(row=1, column= 2, sticky=tkinter.W + tkinter.E)

btn1 = tkinter.Button(frm, text="7")
btn1.grid(row=3, column= 0, sticky=tkinter.W + tkinter.E)

btn1 = tkinter.Button(frm, text="8")
btn1.grid(row=3, column= 1, sticky=tkinter.W + tkinter.E)

btn1 = tkinter.Button(frm, text="9")
btn1.grid(row=3, column= 2, sticky=tkinter.W + tkinter.E)

frm.pack(fill = "x")

root.mainloop()