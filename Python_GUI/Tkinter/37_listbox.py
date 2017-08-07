#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

langs = ("Assembler", "Basic", "Brainfuck", "C", "Python")

listbox = tkinter.Listbox(root)


for lang in langs:
    listbox.insert(tkinter.END, lang)


quitButton = ttk.Button(root, text="Exit", command=exit)

listbox.pack()
quitButton.pack()

root.mainloop()
