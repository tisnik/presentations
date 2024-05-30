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


root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=256, height=256)
canvas.pack()

canvas.create_oval(10, 10, 110, 110, tags="ovals")
canvas.create_oval(150, 10, 250, 110, tags="ovals")
canvas.create_oval(10, 150, 110, 250, tags="ovals")
canvas.create_oval(150, 150, 250, 250, tags="ovals")

canvas.itemconfig("ovals", fill="blue")

root.mainloop()
