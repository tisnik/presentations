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

from tkinter.scrolledtext import *


def exit():
    sys.exit(0)


root = tkinter.Tk()

text = ScrolledText(root, font="Helvetica 14", wrap=tkinter.WORD, width=40, height=24)

text.tag_configure("underlined_red", foreground="red", underline=True)
text.tag_configure("big_green", foreground="green", font="Helvetica 40")
text.tag_configure("blue", foreground="blue")
text.tag_configure("magenta", foreground="magenta")
text.tag_configure("cyan", foreground="cyan")
text.tag_configure("small_yellow", foreground="yellow", font="Helvetica 10")
text.tag_configure("brown", foreground="brown")
text.tag_configure("pink", foreground="pink")
text.tag_configure("white", foreground="white", font="Courier 20")
text.tag_configure("raised", relief=tkinter.RAISED, borderwidth=2)
text.tag_configure("sunken", relief=tkinter.SUNKEN, borderwidth=2)
text.tag_configure("center", justify=tkinter.CENTER)
text.tag_configure("left", justify=tkinter.LEFT)
text.tag_configure("right", justify=tkinter.RIGHT)
text.tag_configure("sup", offset="3p")
text.tag_configure("sub", offset="-3p")

# chovani pri prejeti kurzorem mysi

text.tag_bind(
    "colorOnEnter",
    "<Any-Enter>",
    lambda e: text.tag_configure("colorOnEnter", background="red"),
)
text.tag_bind(
    "colorOnEnter",
    "<Any-Leave>",
    lambda e: text.tag_configure("colorOnEnter", background=""),
)

# chovani pri stisku leveho a praveho tlacitka

text.tag_bind(
    "colorOnEnter",
    "<Button-1>",
    lambda e: text.tag_configure("colorOnEnter", foreground="blue"),
)
text.tag_bind(
    "colorOnEnter",
    "<Button-3>",
    lambda e: text.tag_configure("colorOnEnter", foreground="black"),
)

checkbutton = tkinter.Checkbutton(
    root, text="Delete Internet?", command=lambda: print("changed")
)

quitButton = tkinter.Button(root, text="Exit", command=exit)

# práce s widgetem
text.insert(tkinter.END, "Underlined Red\n", "underlined_red")
text.insert(tkinter.END, "Magenta\n", "magenta")
text.insert(tkinter.END, "Blue\n", "blue")

text.window_create(tkinter.END, window=checkbutton)

text.insert(tkinter.END, "\nCyan\n", "cyan")
text.insert(tkinter.END, "Big Green\n", "big_green")
text.insert(tkinter.END, "active-text", "colorOnEnter")
text.insert(tkinter.END, "Small Yellow\n", "small_yellow")
text.insert(tkinter.END, "Brown\n", "brown")

text.window_create(tkinter.END, window=quitButton)

text.insert(tkinter.END, "Pink\n", "pink")
text.insert(tkinter.END, "White\n", "white")
text.insert(tkinter.END, "Raised box\n", "raised")
text.insert(tkinter.END, "\n")
text.insert(tkinter.END, "Sunken box\n", "sunken")
text.insert(tkinter.END, "\n")
text.insert(tkinter.END, "Centered text\n", "center")
text.insert(tkinter.END, "Left justificiation\n", "left")
text.insert(tkinter.END, "Right justificiation\n", "right")
text.insert(tkinter.END, "H")
text.insert(tkinter.END, "2", "sub")
text.insert(tkinter.END, "O\n")
text.insert(tkinter.END, "E=mc")
text.insert(tkinter.END, "2\n", "sup")
text.insert(tkinter.END, "active-text", "colorOnEnter")

radio_var = tkinter.StringVar()

radio1 = tkinter.Radiobutton(
    root, variable=radio_var, value="Assembler", text="Assembler"
)

radio2 = tkinter.Radiobutton(root, variable=radio_var, value="Basic", text="Basic")

radio3 = tkinter.Radiobutton(
    root, variable=radio_var, value="Brainfuck", text="Brainfuck"
)

radio4 = tkinter.Radiobutton(root, variable=radio_var, value="C", text="C")

radio5 = tkinter.Radiobutton(root, variable=radio_var, value="Python", text="Python")

text.insert(tkinter.END, "\nMaly vyber:\n")
text.window_create(tkinter.END, window=radio1)
text.window_create(tkinter.END, window=radio2)
text.window_create(tkinter.END, window=radio3)
text.window_create(tkinter.END, window=radio4)
text.window_create(tkinter.END, window=radio5)

button = tkinter.Button(root, text="Close window", command=exit)

text.pack()
button.pack()

root.mainloop()
