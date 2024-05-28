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

root = tkinter.Tk()

selected_lang = tkinter.StringVar()

langs = (
    "Assembler",
    "Basic",
    "Brainfuck",
    "C",
    "C++",
    "Java",
    "Julia",
    "Perl",
    "Python",
)

spinbox = tkinter.Spinbox(
    root, values=langs, width=10, textvariable=selected_lang, wrap=True
)

showButton = ttk.Button(
    root, text="Show var", command=lambda: print(selected_lang.get())
)

quitButton = ttk.Button(root, text="Exit", command=exit)

spinbox.grid(column=1, row=1)
showButton.grid(column=1, row=2)
quitButton.grid(column=2, row=2)

root.mainloop()
