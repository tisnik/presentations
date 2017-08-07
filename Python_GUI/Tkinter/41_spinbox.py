#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

number = tkinter.IntVar()

spinbox = tkinter.Spinbox(root, from_=100, to=120, width=10,
                          textvariable=number)

showButton = ttk.Button(root, text="Show var",
                        command=lambda: print(number.get()))

quitButton = ttk.Button(root, text="Exit", command=exit)

spinbox.grid(column=1, row=1)
showButton.grid(column=1, row=2)
quitButton.grid(column=2, row=2)

root.mainloop()
