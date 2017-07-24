#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

import sys

root = Tk()

button1 = ttk.Button(root, text="First button")
button2 = ttk.Button(root, text="Second button with long text")
button3 = ttk.Button(root, text="Third button")
button4 = ttk.Button(root, text="Fourth button")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
