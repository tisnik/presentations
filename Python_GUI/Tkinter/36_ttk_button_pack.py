#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

style = ttk.Style()
style.theme_use("alt")
style.configure('Red.TButton', background='#ff8080')

radio_var = tkinter.StringVar()
radio_var.set("Python")

langs = ("Assembler", "Basic", "Brainfuck", "C", "Python")

radio_buttons = (ttk.Radiobutton(root, text=lang, value=lang,
                                 variable=radio_var)
                 for lang in langs)

showButton = ttk.Button(root, text="Show var",
                        command=lambda: print(radio_var.get()))

quitButton = ttk.Button(root, text="Exit", style='Red.TButton',
                        command=exit)

for radio_button in radio_buttons:
    radio_button.pack(fill="x")

showButton.pack()
quitButton.pack()

root.mainloop()
