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

canvas.create_line(10, 50, 90, 50)
canvas.create_line(110, 50, 190, 50, arrow=tkinter.FIRST)
canvas.create_line(210, 50, 290, 50, arrow=tkinter.LAST)
canvas.create_line(310, 50, 390, 50, arrow=tkinter.BOTH)

canvas.create_line(
    10,
    150,
    90,
    150,
    width=5,
)
canvas.create_line(110, 150, 190, 150, width=5, arrow=tkinter.FIRST)
canvas.create_line(210, 150, 290, 150, width=5, arrow=tkinter.LAST)
canvas.create_line(310, 150, 390, 150, width=5, arrow=tkinter.BOTH)

canvas.create_line(
    10, 250, 90, 250, width=2, arrow=tkinter.LAST, arrowshape=(10, 10, 10)
)
canvas.create_line(
    110, 250, 190, 250, width=2, arrow=tkinter.LAST, arrowshape=(10, 20, 10)
)
canvas.create_line(
    210, 250, 290, 250, width=2, arrow=tkinter.LAST, arrowshape=(10, 5, 10)
)
canvas.create_line(
    310, 250, 390, 250, width=2, arrow=tkinter.LAST, arrowshape=(10, 0, 10)
)

canvas.create_line(
    10, 350, 90, 350, width=2, arrow=tkinter.BOTH, arrowshape=(10, 10, 10)
)
canvas.create_line(
    110, 350, 190, 350, width=2, arrow=tkinter.BOTH, arrowshape=(10, 20, 10)
)
canvas.create_line(
    210, 350, 290, 350, width=2, arrow=tkinter.BOTH, arrowshape=(10, 5, 10)
)
canvas.create_line(
    310, 350, 390, 350, width=2, arrow=tkinter.BOTH, arrowshape=(10, 0, 10)
)

root.mainloop()
