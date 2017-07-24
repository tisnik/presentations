#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

import sys

root = Tk()

button1 = ttk.Button(root, text="1st btn", command=lambda: sys.exit(0))
button2 = ttk.Button(root, text="Second button", command=lambda: sys.exit(0))
button3 = ttk.Button(root, text="Third button", command=lambda: sys.exit(0))
button4 = ttk.Button(root, text="This is fourth button, the last one",
                     command=lambda: sys.exit(0))

button1.grid(column=1, row=1)
button2.grid(column=2, row=1)
button3.grid(column=1, row=2)
button4.grid(column=2, row=2)

root.mainloop()
