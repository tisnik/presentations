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


root = tkinter.Tk()

image = tkinter.BitmapImage(file="test.xbm", foreground="white")
photo_image = tkinter.PhotoImage(file="icons/application-exit.gif")

text = tkinter.Text(
    root,
    font="Helvetica 20",
    wrap=tkinter.WORD,
    background="#202020",
    width=40,
    height=16,
)

text.tag_configure("underlined_red", foreground="red", underline=True)
text.tag_configure("big_green", foreground="green", font="Helvetica 40")
text.tag_configure("blue", foreground="blue")
text.tag_configure("magenta", foreground="magenta")
text.tag_configure("cyan", foreground="cyan")
text.tag_configure("small_yellow", foreground="yellow", font="Helvetica 10")
text.tag_configure("brown", foreground="brown")
text.tag_configure("pink", foreground="pink")
text.tag_configure("white", foreground="white", font="Courier 20")

# práce s widgetem
text.insert(tkinter.END, "Underlined Red\n", "underlined_red")
text.insert(tkinter.END, "Magenta\n", "magenta")
text.insert(tkinter.END, "Blue\n", "blue")
text.insert(tkinter.END, "Cyan\n", "cyan")
text.insert(tkinter.END, "Big Green\n", "big_green")
text.insert(tkinter.END, "Small Yellow\n", "small_yellow")
text.image_create(tkinter.END, image=image)
text.insert(tkinter.END, "Brown\n", "brown")
text.insert(tkinter.END, "Pink    ", "pink")
text.image_create(tkinter.END, image=photo_image)
text.insert(tkinter.END, "White", "white")

button = tkinter.Button(root, text="Close window", command=exit)

text.pack()
button.pack()

root.mainloop()
