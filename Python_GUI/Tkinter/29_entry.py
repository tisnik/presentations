#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

style = ttk.Style()
style.theme_use("alt")
style.configure('Red.TButton', background='#ff8080')

entry = ttk.Entry(root)
entry.insert(0, "xyzzy")

quitButton = ttk.Button(root, text="Exit", style='Red.TButton',
                        command=exit)

entry.grid(column=1, row=1, sticky="we", padx=6, pady=6)
quitButton.grid(column=1, row=2, sticky="we", padx=6, pady=6)

root.mainloop()
