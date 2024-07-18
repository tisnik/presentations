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

root = tkinter.Tk()

style = ttk.Style()
style.theme_use("alt")
style.configure("Red.TButton", background="#ff8080")

value = tkinter.StringVar()

entry = ttk.Entry(root, textvariable=value)
entry.insert(0, "xyzzy")

showButton = ttk.Button(root, text="Show var", command=lambda: print(value.get()))

quitButton = ttk.Button(root, text="Exit", style="Red.TButton", command=exit)

entry.grid(column=1, row=1, sticky="we", padx=6, pady=6)
showButton.grid(column=1, row=2, sticky="we", padx=6, pady=6)
quitButton.grid(column=1, row=3, sticky="we", padx=6, pady=6)

root.mainloop()
