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

canvas.create_rectangle(10, 30, 90, 70, fill="#ff8080", width=2, activefill="white")

canvas.create_rectangle(
    110, 30, 190, 70, fill="#ff8080", width=2, dash=(5, 5), activedash=1
)

canvas.create_rectangle(30, 110, 70, 190, fill="#ff8080", activeoutline="yellow")

canvas.create_rectangle(
    20, 220, 80, 280, fill="#ff8080", activeoutline="yellow", activewidth="5"
)

canvas.create_oval(130, 110, 170, 190, fill="#8080ff", width=2, activedash=(10, 10))

canvas.create_oval(120, 220, 180, 280, fill=None, activefill="#8080ff")

canvas.create_rectangle(210, 30, 290, 70, fill=None, width=2, activefill="white")

canvas.create_rectangle(310, 30, 390, 70, fill=None, width=2, dash=(5, 5), activedash=1)

canvas.create_rectangle(230, 110, 270, 190, fill=None, activeoutline="yellow", width=5)

canvas.create_rectangle(
    220, 220, 280, 280, fill=None, activeoutline="yellow", activewidth="5"
)

canvas.create_oval(330, 110, 370, 190, fill=None, width=2, activedash=(10, 10))

canvas.create_oval(320, 220, 380, 280, fill=None, activefill="#8080ff", width=5)

canvas.create_line(10, 330, 90, 370, fill="#80ff80", width=2, activefill="white")

canvas.create_line(110, 330, 190, 370, fill="#80ff80", width=20, activefill="white")

canvas.create_line(
    210, 330, 290, 370, fill="#80ff80", width=20, activefill="white", dash=10
)


root.mainloop()
