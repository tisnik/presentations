#!/usr/bin/env python

import tkinter
from tkinter import filedialog
import sys


def exit():
    sys.exit(0)


def saveFileDialog():
    filetypes = [('Python sources', '*.py'),
                 ('Lua sources', '*.lua'),
                 ('All files', '*')]
    dialog = filedialog.SaveAs(root, filetypes=filetypes)
    print(dialog.show())


root = tkinter.Tk()

saveFileButton = tkinter.Button(root,
                                text="Save as file dialog",
                                command=saveFileDialog)

quitButton = tkinter.Button(root, text="Exit", command=exit)

saveFileButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
