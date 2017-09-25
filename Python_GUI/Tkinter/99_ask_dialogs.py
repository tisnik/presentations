#!/usr/bin/env python

import tkinter
from tkinter import ttk
from tkinter import messagebox
import sys


def exit():
    sys.exit(0)


def showOkCancelMessageBox():
    print(messagebox.askokcancel("Otázečka na závěr",
                                 "Skutečně, ale skutečně ukončit program?"))


def showRetryCancelMessageBox():
    print(messagebox.askretrycancel("Chyba při tisku",
                                    "Opakovat tisk?"))


def showYesNoMessageBox():
    print(messagebox.askyesno("Otázečka na závěr",
                              "Skutečně, ale skutečně ukončit program?"))


def showQuestionMessageBox():
    print(messagebox.askquestion("Otázečka na závěr",
                                 "Provést zálohu?"))


root = tkinter.Tk()

showOkCancelButton = tkinter.Button(root, text="Show Ok/Cancel message box",
                                    command=showOkCancelMessageBox)

showRetryCancelButton = tkinter.Button(root, text="Show Retry/Cancel box",
                                       command=showRetryCancelMessageBox)

showYesNoButton = tkinter.Button(root, text="Show Yes.No box",
                                 command=showYesNoMessageBox)

showQuestionButton = tkinter.Button(root, text="Show question box",
                                    command=showQuestionMessageBox)

quitButton = tkinter.Button(root, text="Exit", command=exit)

showOkCancelButton.pack(fill=tkinter.BOTH)
showRetryCancelButton.pack(fill=tkinter.BOTH)
showYesNoButton.pack(fill=tkinter.BOTH)
showQuestionButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
