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

canvas.create_line(10, 110, 90, 190, width=2, dash=(12, 3))
canvas.create_line(110, 110, 190, 190, width=2, dash=(9, 6))
canvas.create_line(210, 110, 290, 190, width=2, dash=(6, 9))
canvas.create_line(310, 110, 390, 190, width=2, dash=(3, 12))

canvas.create_line(10, 210, 90, 290, width=2, dash=(12, 2, 2, 2))
canvas.create_line(110, 210, 190, 290, width=2, dash=(12, 2, 4, 2))
canvas.create_line(210, 210, 290, 290, width=2, dash=(12, 4, 2, 4))
canvas.create_line(310, 210, 390, 290, width=2, dash=(12, 2, 2, 2, 2, 2))

canvas.create_line(10, 310, 90, 390, width=2, dash=(12, 2, 2, 2), dashoff=0)
canvas.create_line(110, 310, 190, 390, width=2, dash=(12, 2, 4, 2), dashoff=5)
canvas.create_line(210, 310, 290, 390, width=2, dash=(12, 4, 2, 4), dashoff=10)
canvas.create_line(310, 310, 390, 390, width=2, dash=(12, 2, 2, 2, 2, 2), dashoff=-5)

root.mainloop()
