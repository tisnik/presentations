#!/usr/bin/env python

import tkinter
from tkinter import ttk


def setcolor(color):
    canvas.itemconfig("current", fill=color)


root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=256, height=256)
canvas.pack()

canvas.create_oval(10, 10, 110, 110, tags="ovals")
canvas.create_oval(150, 10, 250, 110, tags="ovals")
canvas.create_oval(10, 150, 110, 250, tags="ovals")
canvas.create_oval(150, 150, 250, 250, tags="ovals")

canvas.itemconfig("ovals", fill="blue")

canvas.tag_bind("ovals", "<Enter>", lambda e: setcolor("red"))
canvas.tag_bind("ovals", "<Leave>", lambda e: setcolor("blue"))
canvas.tag_bind("ovals", "<Button-1>", lambda e: setcolor("yellow"))

root.mainloop()
