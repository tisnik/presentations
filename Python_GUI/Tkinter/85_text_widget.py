#!/usr/bin/env python

import tkinter
from tkinter import ttk
import sys


def exit():
    sys.exit(0)


root = tkinter.Tk()

text = tkinter.Text(root)

text.insert(tkinter.END, "Test widgetu\n'text'")

button = tkinter.Button(root, text="Close window", command=exit)

text.pack()
button.pack()

root.mainloop()
