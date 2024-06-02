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
from tkinter import messagebox
import sys


def exit():
    sys.exit(0)


root = tkinter.Tk()


infoButton = tkinter.Button(
    root, text="Info box", command=lambda: messagebox.showinfo("Title", "Text")
)

warningButton = tkinter.Button(
    root, text="Warning box", command=lambda: messagebox.showwarning("Title", "Text")
)

errorButton = tkinter.Button(
    root, text="Error box", command=lambda: messagebox.showerror("Title", "Text")
)

quitButton = tkinter.Button(root, text="Exit", command=exit)

infoButton.pack(fill=tkinter.BOTH)
warningButton.pack(fill=tkinter.BOTH)
errorButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
