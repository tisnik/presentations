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


root = tkinter.Tk()

menubar = tkinter.Menu(root)

filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(
    label="Open", underline=0, accelerator="Ctrl+O", command=lambda: print("Open")
)
filemenu.add_command(
    label="Save", underline=0, accelerator="Ctrl+S", command=lambda: print("Save")
)
filemenu.add_separator()
filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu, underline=0)

editmenu = tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(
    label="Undo", underline=0, accelerator="Ctrl+U", command=lambda: print("Undo")
)
editmenu.add_separator()
editmenu.add_command(
    label="Cut", underline=2, accelerator="Ctrl+X", command=lambda: print("Cut")
)
editmenu.add_command(
    label="Copy", underline=0, accelerator="Ctrl+C", command=lambda: print("Copy")
)
editmenu.add_command(
    label="Paste", underline=0, accelerator="Ctrl+V", command=lambda: print("Paste")
)
editmenu.add_command(label="Delete", underline=2, command=lambda: print("Delete"))
editmenu.add_separator()
editmenu.add_command(
    label="Select All",
    underline=7,
    accelerator="Ctrl+A",
    command=lambda: print("Select All"),
)
menubar.add_cascade(label="Edit", menu=editmenu, underline=0)

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(
    label="About", underline=0, accelerator="F1", command=lambda: print("About")
)
menubar.add_cascade(label="Help", menu=helpmenu, underline=0)

root.config(menu=menubar)

root.mainloop()
