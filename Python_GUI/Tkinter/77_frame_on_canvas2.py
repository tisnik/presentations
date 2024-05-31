#!/usr/bin/env python

#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import tkinter
from tkinter import ttk
import sys


def exit():
    sys.exit(0)


root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=300, height=300, background="white")
canvas.pack()

canvas.create_line(0, 150, 80, 20, 220, 280, 300, 150, dash=10)

canvas.create_line(0, 150, 80, 20, 220, 280, 300, 150, smooth=True, width=2, fill="red")

nested_window = tkinter.Frame(relief=tkinter.RAISED)
canvas.create_window(150, 150, width=150, height=150, window=nested_window)

label = tkinter.Label(nested_window, text="Hello world!")
button = tkinter.Button(nested_window, text="Close window", command=exit)

label.pack()
button.pack()

root.mainloop()
