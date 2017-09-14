#!/usr/bin/env python

import tkinter
from tkinter import ttk
import sys


def exit():
    sys.exit(0)


root = tkinter.Tk()

text = tkinter.Text(root,
                    font="Helvetica 20",
                    foreground="#0000c0",
                    background="#c0ffc0",
                    selectforeground="white",
                    selectbackground="red",
                    insertwidth=4,
                    insertbackground="red",
                    insertborderwidth=1,
                    wrap=tkinter.WORD,
                    width=40, height=16)

text.insert(tkinter.END, "Test widgetu\n'text'")

button = tkinter.Button(root, text="Close window", command=exit)

text.pack()
button.pack()

root.mainloop()
