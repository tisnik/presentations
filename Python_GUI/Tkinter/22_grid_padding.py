#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys


def exit():
    sys.exit(0)


root = tkinter.Tk()

style = ttk.Style()
style.configure('Red.TButton', background='#ff8080')

buttonStyles = ("sunken", "solid", "flat", "groove", "raised", "ridge")

buttons = (tkinter.Button(root, text=buttonStyle, relief=buttonStyle)
           for buttonStyle in buttonStyles)

quitButton = ttk.Button(root, text="Exit", style='Red.TButton',
                        command=exit)

for i, button in enumerate(buttons):
    button.grid(column=1, row=i, sticky="we", padx=6, pady=6)

quitButton.grid(column=2, row=6, sticky="we", padx=6, pady=6)

root.mainloop()
