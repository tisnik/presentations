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


def draw_text(canvas, x, y, anchor):
    canvas.create_text(
        x, y, text="Test", fill="gray", anchor=anchor, font="Helvetica 16"
    )
    canvas.create_line(x - 5, y, x + 5, y, fill="red")
    canvas.create_line(x, y - 5, x, y + 5, fill="red")


root = tkinter.Tk()

canvas = basic_canvas(root, WIDTH, HEIGHT, GRID_SIZE)

draw_text(canvas, 50, 50, "ne")
draw_text(canvas, 150, 50, "n")
draw_text(canvas, 250, 50, "nw")

draw_text(canvas, 50, 150, "e")
draw_text(canvas, 150, 150, "center")
draw_text(canvas, 250, 150, "w")

draw_text(canvas, 50, 250, "se")
draw_text(canvas, 150, 250, "s")
draw_text(canvas, 250, 250, "sw")

root.mainloop()
