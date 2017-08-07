#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

selected_lang = tkinter.StringVar()

langs = ("Assembler", "Basic", "Brainfuck", "C", "C++", "Java", "Julia",
         "Perl", "Python")

spinbox = tkinter.Spinbox(root, values=langs, width=10,
                          textvariable=selected_lang, wrap=True)

showButton = ttk.Button(root, text="Show var",
                        command=lambda: print(selected_lang.get()))

quitButton = ttk.Button(root, text="Exit", command=exit)

spinbox.grid(column=1, row=1)
showButton.grid(column=1, row=2)
quitButton.grid(column=2, row=2)

root.mainloop()
