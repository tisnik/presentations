#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

style = ttk.Style()
style.theme_use("alt")
style.configure('Red.TButton', background='#ff8080')

checkbutton = ttk.Checkbutton(root, text="Delete Internet?",
                              command=lambda: print("changed"))

quitButton = ttk.Button(root, text="Exit", style='Red.TButton',
                        command=exit)

checkbutton.grid(column=1, row=1, sticky="we", padx=6, pady=6)
quitButton.grid(column=1, row=2, sticky="we", padx=6, pady=6)

root.mainloop()
