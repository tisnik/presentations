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

from tkinter import *
from tkinter import ttk

import sys

root = Tk()

button1 = ttk.Button(root, text="First button", command=lambda: sys.exit(0))
button2 = ttk.Button(root, text="Second button", command=lambda: sys.exit(0))
button3 = ttk.Button(root, text="Third button", command=lambda: sys.exit(0))
button4 = ttk.Button(root, text="Fourth button", command=lambda: sys.exit(0))

button1.grid(column=1, row=1)
button2.grid(column=2, row=2)
button3.grid(column=1, row=3, columnspan=2)
button4.grid(column=4, row=1, rowspan=3)

root.mainloop()
