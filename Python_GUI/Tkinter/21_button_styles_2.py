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
style.configure("Red.TButton", background="#ff8080")

buttonStyles = ("sunken", "solid", "flat", "groove", "raised", "ridge")

buttons = (
    tkinter.Button(root, text=buttonStyle, relief=buttonStyle)
    for buttonStyle in buttonStyles
)

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

for i, button in enumerate(buttons):
    button.grid(column=1, row=i, sticky="we")

quitButton.grid(column=2, row=6, sticky="we")

root.mainloop()
