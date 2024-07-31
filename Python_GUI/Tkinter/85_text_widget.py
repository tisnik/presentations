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

text = tkinter.Text(root)

text.insert(tkinter.END, "Test widgetu\n'text'")

button = tkinter.Button(root, text="Close window", command=exit)

text.pack()
button.pack()

root.mainloop()
