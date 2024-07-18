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
from tkinter import colorchooser


def exit():
    sys.exit(0)


def chooseColorDialog():
    rgb_values, hexa_triplet = colorchooser.askcolor(
        color="lightgreen", title="Please select any color"
    )
    print(rgb_values)
    print(hexa_triplet)


root = tkinter.Tk()

chooseColorButton = tkinter.Button(root, text="Choose color", command=chooseColorDialog)

quitButton = tkinter.Button(root, text="Exit", command=exit)

chooseColorButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
