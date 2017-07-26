#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

import sys


def exit():
    sys.exit(0)


root = Tk()

style = ttk.Style()
style.configure('Red.TButton', background='#ff8080')

button1 = ttk.Button(root, text="1s button", command=exit)
button2 = ttk.Button(root, text="2nd button with long text", command=exit)
button3 = ttk.Button(root, text="3rd button", command=exit)
button4 = ttk.Button(root, text="4th button", command=exit)

quitButton = ttk.Button(root, text="Exit", style='Red.TButton',
                        command=exit)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

label = Label(root, text='Hello world')
entry = Entry(root)
checkbutton = Checkbutton(text='Do you like Tkinter?')

checkbutton.pack()
label.pack()
entry.pack()

quitButton.pack()

root.mainloop()
