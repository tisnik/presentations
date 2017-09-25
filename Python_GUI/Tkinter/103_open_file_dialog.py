#!/usr/bin/env python

import tkinter
from tkinter import filedialog
import sys


def exit():
    sys.exit(0)


def openFileDialog():
    filetypes = [('Python sources', '*.py'),
                 ('Lua sources', '*.lua'),
                 ('All files', '*')]
    dialog = filedialog.Open(root, filetypes=filetypes)
    print(dialog.show())


root = tkinter.Tk()

openFileButton = tkinter.Button(root,
                                text="Open file dialog",
                                command=openFileDialog)

quitButton = tkinter.Button(root, text="Exit", command=exit)

openFileButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
