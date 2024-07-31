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

canvas.create_rectangle(10, 30, 90, 70, fill="#ff8080")

canvas.create_rectangle(30, 110, 70, 190, fill="#ff8080")

canvas.create_rectangle(20, 220, 80, 280, fill="#ff8080")

canvas.create_oval(110, 30, 190, 70, fill="#8080ff")

canvas.create_oval(130, 110, 170, 190, fill="#8080ff")

canvas.create_oval(120, 220, 180, 280, fill="#8080ff")

canvas.create_polygon(210, 20, 290, 20, 250, 80, fill="#ffff80")

canvas.create_polygon(310, 20, 390, 20, 350, 80, fill="#ffff80", outline="black")

canvas.create_polygon(210, 120, 250, 140, 290, 120, 250, 180, fill="#80ff80")

canvas.create_polygon(
    310, 120, 350, 140, 390, 120, 350, 180, fill="#80ff80", outline="black"
)

canvas.create_polygon(210, 220, 290, 220, 250, 280, fill="#ffff80", smooth=1)

canvas.create_polygon(
    310, 220, 390, 220, 350, 280, fill="#ffff80", outline="black", smooth=1
)

canvas.create_polygon(210, 320, 250, 340, 290, 320, 250, 380, fill="#80ff80", smooth=1)

canvas.create_polygon(
    310, 320, 350, 340, 390, 320, 350, 380, fill="#80ff80", outline="black", smooth=1
)


root.mainloop()
