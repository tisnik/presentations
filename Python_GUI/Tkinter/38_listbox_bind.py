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

langs = ("Assembler", "Basic", "Brainfuck", "C", "Python")

listbox = tkinter.Listbox(root)


for lang in langs:
    listbox.insert(tkinter.END, lang)


def on_listbox_select(event):
    index = listbox.curselection()[0]
    global langs
    print(langs[index])


listbox.bind("<<ListboxSelect>>", on_listbox_select)

quitButton = ttk.Button(root, text="Exit", command=exit)

listbox.pack()
quitButton.pack()

root.mainloop()
