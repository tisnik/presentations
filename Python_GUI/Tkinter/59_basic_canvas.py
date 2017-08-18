#!/usr/bin/env python

import tkinter
from tkinter import ttk


root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=256, height=256)
canvas.pack()

canvas.create_oval(10, 10, 100, 100)
canvas.create_line(0, 0, 255, 255)
canvas.create_line(0, 255, 255, 0)

canvas.create_text(50, 120, text="Hello world!")

root.mainloop()
