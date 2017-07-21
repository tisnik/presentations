#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

import sys


def exit():
    sys.exit(0)


root = Tk()

style = ttk.Style()

for style_name in ('clam', 'alt', 'default', 'classic'):
    style.theme_use(style_name)
    style.configure('Red.TButton', background='#ff8080')

button1 = ttk.Button(root, text="clam",
                     command=lambda: style.theme_use("clam"))
button2 = ttk.Button(root, text="alt",
                     command=lambda: style.theme_use("alt"))
button3 = ttk.Button(root, text="default",
                     command=lambda: style.theme_use("default"))
button4 = ttk.Button(root, text="classic",
                     command=lambda: style.theme_use("classic"))

quitButton = ttk.Button(root, text="Exit", style='Red.TButton',
                        command=exit)

button1.grid(column=1, row=1, sticky="we")
button2.grid(column=2, row=1, sticky="we")
button3.grid(column=1, row=2, sticky="we")
button4.grid(column=2, row=2, sticky="we")

quitButton.grid(column=2, row=5, sticky="we")

label = Label(root, text='Hello world')
entry = Entry(root)
checkbutton = Checkbutton(text='Do you like Tkinter?')

checkbutton.grid(column=1, row=3, columnspan=2, sticky="w")
label.grid(column=1, row=4)
entry.grid(column=2, row=4)

root.mainloop()
