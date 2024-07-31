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

import sys
import tkinter
from tkinter import ttk

WIDTH = 400
HEIGHT = 400
GRID_SIZE = 100


def exit():
    sys.exit(0)


def basic_canvas(root, width, height, grid_size):
    canvas = tkinter.Canvas(root, width=width, height=height, background="#ccffcc")
    canvas.pack()

    draw_grid(canvas, width, height, grid_size)
    return canvas


def draw_grid(canvas, width, height, grid_size):
    for x in range(0, width, grid_size):
        canvas.create_line(x, 0, x, height, dash=7, fill="gray")
    for y in range(0, height, grid_size):
        canvas.create_line(0, y, width, y, dash=7, fill="gray")


root = tkinter.Tk()

canvas = basic_canvas(root, WIDTH, HEIGHT, GRID_SIZE)

canvas.create_line(0, 0, 100, 100, fill="red", width=2, dash=8)

canvas.create_arc(
    100, 1, 200, 100, outline="blue", start=45, extent=180, style=tkinter.ARC, width=2
)

canvas.create_oval(200, 1, 300, 100)

canvas.create_oval(325, 25, 375, 75, fill="#a0a0ff")

canvas.create_rectangle(50, 125, 150, 175, fill="#a0a0ff")

canvas.create_text(300, 150, text="Hello world!", font="Helvetica 20")

canvas.create_polygon(50, 225, 200, 300, 50, 375, fill="#80ff80")

canvas.create_polygon(
    250, 225, 400, 300, 250, 375, fill="black", outline="red", width="5"
)

root.mainloop()
