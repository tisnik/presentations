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

canvas.create_oval(10, 10, 100, 100)
canvas.create_line(0, 0, 255, 255)
canvas.create_line(0, 255, 255, 0)

canvas.create_text(50, 120, text="Hello world!")

root.mainloop()
