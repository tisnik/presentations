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
from tkinter import filedialog


def exit():
    sys.exit(0)


def saveFileDialog():
    filetypes = [
        ("Python sources", "*.py"),
        ("Lua sources", "*.lua"),
        ("All files", "*"),
    ]
    dialog = filedialog.SaveAs(root, filetypes=filetypes)
    print(dialog.show())


root = tkinter.Tk()

saveFileButton = tkinter.Button(
    root, text="Save as file dialog", command=saveFileDialog
)

quitButton = tkinter.Button(root, text="Exit", command=exit)

saveFileButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
