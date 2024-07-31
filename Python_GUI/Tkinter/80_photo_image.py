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


image_names = [
    "document-open",
    "document-save",
    "application-exit",
    "edit-undo",
    "edit-cut",
    "edit-copy",
    "edit-paste",
    "edit-delete",
    "edit-select-all",
]

root = tkinter.Tk()

images = {}
for image_name in image_names:
    images[image_name] = tkinter.PhotoImage(file="icons/%s.gif" % image_name)

canvas = basic_canvas(root, WIDTH, HEIGHT, GRID_SIZE)

canvas.create_image((50, 50), image=images["document-open"])
canvas.create_image((150, 50), image=images["document-save"])
canvas.create_image((250, 50), image=images["application-exit"])
canvas.create_image((50, 150), image=images["edit-undo"])
canvas.create_image((150, 150), image=images["edit-cut"])
canvas.create_image((250, 150), image=images["edit-copy"])
canvas.create_image((50, 250), image=images["edit-paste"])
canvas.create_image((150, 250), image=images["edit-delete"])
canvas.create_image((250, 250), image=images["edit-select-all"])

root.mainloop()
