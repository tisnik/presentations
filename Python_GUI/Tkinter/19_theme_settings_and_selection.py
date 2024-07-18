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

style = ttk.Style()

for style_name in ("clam", "alt", "default", "classic"):
    style.theme_use(style_name)
    style.configure("Red.TButton", background="#ff8080")

button1 = ttk.Button(root, text="clam", command=lambda: style.theme_use("clam"))
button2 = ttk.Button(root, text="alt", command=lambda: style.theme_use("alt"))
button3 = ttk.Button(root, text="default", command=lambda: style.theme_use("default"))
button4 = ttk.Button(root, text="classic", command=lambda: style.theme_use("classic"))

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

button1.grid(column=1, row=1, sticky="we")
button2.grid(column=2, row=1, sticky="we")
button3.grid(column=1, row=2, sticky="we")
button4.grid(column=2, row=2, sticky="we")

quitButton.grid(column=2, row=5, sticky="we")

label = tkinter.Label(root, text="Hello world")
entry = tkinter.Entry(root)
checkbutton = tkinter.Checkbutton(text="Do you like Tkinter?")

checkbutton.grid(column=1, row=3, columnspan=2, sticky="w")
label.grid(column=1, row=4)
entry.grid(column=2, row=4)

root.mainloop()
