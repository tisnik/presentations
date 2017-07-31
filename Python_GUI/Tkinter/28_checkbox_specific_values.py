#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

style = ttk.Style()
style.theme_use("alt")
style.configure('Red.TButton', background='#ff8080')

delete_internet = tkinter.StringVar()

checkbutton = ttk.Checkbutton(root, text="Delete Internet?",
                              variable=delete_internet,
                              onvalue="yes",
                              offvalue="no",
                              command=lambda: print(delete_internet.get()))

quitButton = ttk.Button(root, text="Exit", style='Red.TButton',
                        command=exit)

checkbutton.grid(column=1, row=1, sticky="we", padx=6, pady=6)
quitButton.grid(column=1, row=2, sticky="we", padx=6, pady=6)

root.mainloop()
