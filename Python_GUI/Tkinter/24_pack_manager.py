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

button1 = ttk.Button(root, text="1s button", command=exit)
button2 = ttk.Button(root, text="2nd button with long text", command=exit)
button3 = ttk.Button(root, text="3rd button", command=exit)
button4 = ttk.Button(root, text="4th button", command=exit)

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

label = tkinter.Label(root, text="Hello world")
entry = tkinter.Entry(root)
checkbutton = tkinter.Checkbutton(text="Do you like Tkinter?")

checkbutton.pack()
label.pack()
entry.pack()

quitButton.pack()

root.mainloop()
