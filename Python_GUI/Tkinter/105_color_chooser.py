#!/usr/bin/env python

import tkinter
from tkinter import colorchooser
import sys


def exit():
    sys.exit(0)


def chooseColorDialog():
    rgb_values, hexa_triplet = colorchooser.askcolor(color="lightgreen",
                                                     title="Please select any color")
    print(rgb_values)
    print(hexa_triplet)


root = tkinter.Tk()

chooseColorButton = tkinter.Button(root,
                                   text="Choose color",
                                   command=chooseColorDialog)

quitButton = tkinter.Button(root, text="Exit", command=exit)

chooseColorButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
