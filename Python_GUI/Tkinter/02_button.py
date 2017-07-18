#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

import sys

def exit():
    sys.exit(0)

root = Tk()

label = ttk.Label(root, text="Hello world!")
button = ttk.Button(root, text="Close window", command=exit)

label.pack()
button.pack()

root.mainloop()

