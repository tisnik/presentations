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

for i, radio_button in enumerate(radio_buttons):
    radio_button.grid(column=1, row=i, sticky="w")

showButton.grid(column=2, row=6, sticky="we", padx=6, pady=6)
quitButton.grid(column=2, row=7, sticky="we", padx=6, pady=6)

root.mainloop()
