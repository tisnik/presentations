#!/usr/bin/env python

import tkinter
from tkinter import ttk


root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=256, height=256)
canvas.pack()

canvas.create_oval(10, 10, 110, 110, tags="ovals", fill="blue")
canvas.create_oval(150, 10, 250, 110, tags="ovals", fill="blue")
canvas.create_oval(10, 150, 110, 250, tags="ovals", fill="blue")
canvas.create_oval(150, 150, 250, 250, tags="ovals", fill="blue")

root.mainloop()
