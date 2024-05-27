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

style = ttk.Style()
style.theme_use("alt")
style.configure("Red.TButton", background="#ff8080")

radio_var = tkinter.StringVar()
radio_var.set("Python")

langs = ("Assembler", "Basic", "Brainfuck", "C", "Python")

radio_buttons = (
    ttk.Radiobutton(root, text=lang, value=lang, variable=radio_var) for lang in langs
)

showButton = ttk.Button(root, text="Show var", command=lambda: print(radio_var.get()))

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

for radio_button in radio_buttons:
    radio_button.pack(fill="x")

showButton.pack()
quitButton.pack()

root.mainloop()
