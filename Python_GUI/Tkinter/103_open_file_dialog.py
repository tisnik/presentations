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
from tkinter import filedialog
import sys


def exit():
    sys.exit(0)


def openFileDialog():
    filetypes = [
        ("Python sources", "*.py"),
        ("Lua sources", "*.lua"),
        ("All files", "*"),
    ]
    dialog = filedialog.Open(root, filetypes=filetypes)
    print(dialog.show())


root = tkinter.Tk()

openFileButton = tkinter.Button(root, text="Open file dialog", command=openFileDialog)

quitButton = tkinter.Button(root, text="Exit", command=exit)

openFileButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
