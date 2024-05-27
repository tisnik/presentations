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

radio1 = ttk.Radiobutton(root, variable=radio_var, value="Assembler", text="Assembler")

radio2 = ttk.Radiobutton(root, variable=radio_var, value="Basic", text="Basic")

radio3 = ttk.Radiobutton(root, variable=radio_var, value="Brainfuck", text="Brainfuck")

radio4 = ttk.Radiobutton(root, variable=radio_var, value="C", text="C")

radio5 = ttk.Radiobutton(root, variable=radio_var, value="Python", text="Python")

showButton = ttk.Button(root, text="Show var", command=lambda: print(radio_var.get()))

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

radio1.grid(column=1, row=1, sticky="w")
radio2.grid(column=1, row=2, sticky="w")
radio3.grid(column=1, row=3, sticky="w")
radio4.grid(column=1, row=4, sticky="w")
radio5.grid(column=1, row=5, sticky="w")

showButton.grid(column=2, row=6, sticky="we", padx=6, pady=6)
quitButton.grid(column=2, row=7, sticky="we", padx=6, pady=6)

root.mainloop()
