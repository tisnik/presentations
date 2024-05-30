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

canvas.create_line(10, 10, 90, 90)
canvas.create_line(110, 10, 190, 90, fill="#8080ff")
canvas.create_line(210, 10, 290, 90, fill="#ffff80", width=8)
canvas.create_line(310, 10, 390, 90, fill="#80aa80", width=8, dash=15)

canvas.create_line(10, 110, 90, 190, fill="red", width=12)
canvas.create_line(110, 110, 190, 190, fill="red", width=12, cap=tkinter.BUTT)
canvas.create_line(210, 110, 290, 190, fill="red", width=12, cap=tkinter.PROJECTING)
canvas.create_line(310, 110, 390, 190, fill="red", width=12, cap=tkinter.ROUND)

canvas.create_line(10, 110, 90, 190, fill="white")
canvas.create_line(110, 110, 190, 190, fill="white")
canvas.create_line(210, 110, 290, 190, fill="white")
canvas.create_line(310, 110, 390, 190, fill="white")

canvas.create_line(10, 210, 50, 290, 90, 210, fill="red", width=12)
canvas.create_line(110, 210, 150, 290, 190, 210, fill="red", width=12, cap=tkinter.BUTT)
canvas.create_line(
    210, 210, 250, 290, 290, 210, fill="red", width=12, cap=tkinter.PROJECTING
)
canvas.create_line(
    310, 210, 350, 290, 390, 210, fill="red", width=12, cap=tkinter.ROUND
)

# pomocne usecky
canvas.create_line(10, 210, 50, 290, 90, 210, fill="white")
canvas.create_line(110, 210, 150, 290, 190, 210, fill="white")
canvas.create_line(210, 210, 250, 290, 290, 210, fill="white")
canvas.create_line(310, 210, 350, 290, 390, 210, fill="white")

canvas.create_line(10, 310, 50, 390, 90, 310, fill="red", width=12)
canvas.create_line(
    110, 310, 150, 390, 190, 310, fill="red", width=12, join=tkinter.ROUND
)
canvas.create_line(
    210, 310, 250, 390, 290, 310, fill="red", width=12, join=tkinter.BEVEL
)
canvas.create_line(
    310, 310, 350, 390, 390, 310, fill="red", width=12, join=tkinter.MITER
)

# pomocne usecky
canvas.create_line(10, 310, 50, 390, 90, 310, fill="white")
canvas.create_line(110, 310, 150, 390, 190, 310, fill="white")
canvas.create_line(210, 310, 250, 390, 290, 310, fill="white")
canvas.create_line(310, 310, 350, 390, 390, 310, fill="white")

root.mainloop()
