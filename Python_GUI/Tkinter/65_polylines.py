#!/usr/bin/env python

import tkinter
from tkinter import ttk


root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_line(0, 150,
                   80, 20,
                   220, 280,
                   300, 150, dash=10)

root.mainloop()
