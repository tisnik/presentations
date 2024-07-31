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

canvas.create_arc(0, 0, 100, 100, outline="red", style=tkinter.ARC, width=2)

canvas.create_arc(
    100, 100, 200, 200, outline="blue", start=45, style=tkinter.ARC, width=2
)

canvas.create_arc(
    200, 0, 300, 100, outline="brown", extent=180, style=tkinter.ARC, width=2
)

canvas.create_arc(
    300,
    100,
    400,
    200,
    outline="green",
    start=45,
    extent=270,
    style=tkinter.ARC,
    width=2,
)

canvas.create_arc(0, 200, 100, 300, outline="red", style=tkinter.ARC, dash=8, width=2)

canvas.create_arc(
    100, 300, 200, 400, outline="blue", start=45, style=tkinter.ARC, dash=8, width=10
)

canvas.create_arc(
    200,
    200,
    300,
    300,
    outline="green",
    start=45,
    extent=270,
    style=tkinter.ARC,
    dash=3,
    width=50,
)

canvas.create_arc(
    290,
    290,
    390,
    390,
    outline="brown",
    extent=270,
    style=tkinter.ARC,
    dash=80,
    width=20,
)

root.mainloop()
