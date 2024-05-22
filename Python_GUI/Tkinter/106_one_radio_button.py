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

import sys


def print_state():
    print(radio_var.get())


root = tkinter.Tk()

radio_var = tkinter.StringVar()

radio1 = tkinter.Radiobutton(
    root, variable=radio_var, value="Radio button", text="Radio button"
)

testButton = tkinter.Button(root, text="Print state", command=print_state)

quitButton = tkinter.Button(root, text="Quit", command=exit)

radio1.grid(column=1, row=1)
testButton.grid(column=1, row=2, sticky="we", padx=6, pady=6)
quitButton.grid(column=1, row=3, sticky="we", padx=6, pady=6)

root.mainloop()
