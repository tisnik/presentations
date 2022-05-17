#!/usr/bin/env python
# vim: set fileencoding=utf-8

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


def test():
    print("Test!")


root = tkinter.Tk()

menubar = tkinter.Menu(root)
menubar.add_command(label="Test", command=test)
menubar.add_command(label="Quit", command=root.quit)

root.config(menu=menubar)

style = ttk.Style()
style.theme_use("alt")
style.configure("Red.TButton", background="#ff8080")

radio_var = tkinter.StringVar()
radio_var.set("Python")

langs = ("Assembler", "Basic", "Brainfuck", "C", "Python")

f1 = ttk.LabelFrame(root, text="Languages")
f2 = ttk.LabelFrame(root, text="Commands")

radio_buttons = (
    ttk.Radiobutton(f1, text=lang, value=lang, variable=radio_var) for lang in langs
)

showButton = ttk.Button(f2, text="Show var", command=lambda: print(radio_var.get()))

quitButton = ttk.Button(f2, text="Exit", style="Red.TButton", command=root.quit)

for i, radio_button in enumerate(radio_buttons):
    radio_button.grid(column=1, row=i, sticky="w")

showButton.grid(column=1, row=1, sticky="we", padx=6, pady=6)
quitButton.grid(column=1, row=2, sticky="we", padx=6, pady=6)

f1.grid(column=1, row=1, sticky="ne", padx=6, pady=6)
f2.grid(column=2, row=1, sticky="ne", padx=6, pady=6)

root.mainloop()
