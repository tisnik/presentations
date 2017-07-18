#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

import sys

root = Tk()

label = ttk.Label(root, text="Hello world!")
button = ttk.Button(root, text="Close window", command=lambda:sys.exit(0))

label.pack()
button.pack()

root.mainloop()

