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
    wrap=tkinter.WORD,
    background="#202020",
    width=40,
    height=16,
)

text.tag_configure("red", foreground="red")
text.tag_configure("green", foreground="green")
text.tag_configure("blue", foreground="blue")
text.tag_configure("magenta", foreground="magenta")
text.tag_configure("cyan", foreground="cyan")
text.tag_configure("yellow", foreground="yellow")
text.tag_configure("brown", foreground="brown")
text.tag_configure("pink", foreground="pink")
text.tag_configure("white", foreground="white")

# práce s widgetem
text.insert(tkinter.END, "Red\n", "red")
text.insert(tkinter.END, "Magenta\n", "magenta")
text.insert(tkinter.END, "Blue\n", "blue")
text.insert(tkinter.END, "Cyan\n", "cyan")
text.insert(tkinter.END, "Green\n", "green")
text.insert(tkinter.END, "Yellow\n", "yellow")
text.insert(tkinter.END, "Brown\n", "brown")
text.insert(tkinter.END, "Pink\n", "pink")
text.insert(tkinter.END, "White\n", "white")

button = tkinter.Button(root, text="Close window", command=exit)

text.pack()
button.pack()

root.mainloop()
