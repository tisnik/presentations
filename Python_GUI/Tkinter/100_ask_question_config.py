#!/usr/bin/env python

import tkinter
from tkinter import ttk
from tkinter import messagebox
import sys


def exit():
    sys.exit(0)


def showQuestionMessageBox():
    print(messagebox.askquestion("Otázečka na závěr",
                                 ("Provést zálohu?\n"
                                  "Naformátovat disk?\n"
                                  "Kontaktovat NSA?"),
                                 icon=messagebox.ERROR,
                                 type=messagebox.ABORTRETRYIGNORE))


root = tkinter.Tk()

showQuestionButton = tkinter.Button(root, text="Show question box",
                                    command=showQuestionMessageBox)

quitButton = tkinter.Button(root, text="Exit", command=exit)

showQuestionButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
