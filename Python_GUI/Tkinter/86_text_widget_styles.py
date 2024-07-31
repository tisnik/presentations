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


def exit():
    sys.exit(0)


root = tkinter.Tk()

text = tkinter.Text(
    root,
    font="Helvetica 20",
    foreground="#0000c0",
    background="#c0ffc0",
    selectforeground="white",
    selectbackground="red",
    insertwidth=4,
    insertbackground="red",
    insertborderwidth=1,
    wrap=tkinter.WORD,
    width=40,
    height=16,
)

text.insert(tkinter.END, "Test widgetu\n'text'")

button = tkinter.Button(root, text="Close window", command=exit)

text.pack()
button.pack()

root.mainloop()
