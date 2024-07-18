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
from tkinter import *
from tkinter import ttk

root = Tk()

button1 = ttk.Button(root, text="First button")
button2 = ttk.Button(root, text="Second button with long text")
button3 = ttk.Button(root, text="Third button")
button4 = ttk.Button(root, text="Fourth button")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
