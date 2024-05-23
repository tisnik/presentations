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


def exit():
    sys.exit(0)


root = tkinter.Tk()

style = ttk.Style()
style.configure("Red.TButton", background="#ff8080")

button1 = tkinter.Button(root, text="sunken", relief="sunken")
button2 = tkinter.Button(root, text="solid", relief="solid")
button3 = tkinter.Button(root, text="flat", relief="flat")
button4 = tkinter.Button(root, text="groove", relief="groove")
button5 = tkinter.Button(root, text="raised", relief="raised")
button6 = tkinter.Button(root, text="ridge", relief="ridge")

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

button1.grid(column=1, row=1, sticky="we")
button2.grid(column=1, row=2, sticky="we")
button3.grid(column=1, row=3, sticky="we")
button4.grid(column=1, row=4, sticky="we")
button5.grid(column=1, row=5, sticky="we")
button6.grid(column=1, row=6, sticky="we")

quitButton.grid(column=2, row=6, sticky="we")

root.mainloop()
