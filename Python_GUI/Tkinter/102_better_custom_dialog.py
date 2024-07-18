#!/usr/bin/env python

#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import sys
import tkinter
from tkinter import messagebox, ttk


def exit():
    sys.exit(0)


class Dialog(tkinter.Toplevel):
    def __init__(self, parent):
        tkinter.Toplevel.__init__(self, parent)

        # dialog bude svazan se svym predkem
        # (nemel by se zobrazit v seznamu oken)
        self.transient(parent)

        label1 = tkinter.Label(self, text="First name")
        label2 = tkinter.Label(self, text="Surname")

        self.entryFirstName = tkinter.Entry(self)
        self.entrySurname = tkinter.Entry(self)

        okButton = tkinter.Button(self, text="OK", command=self.ok)

        label1.grid(row=1, column=1, sticky="W", padx=5, pady=5)
        label2.grid(row=2, column=1, sticky="W", padx=5, pady=5)
        self.entryFirstName.grid(row=1, column=2, sticky="WE")
        self.entrySurname.grid(row=2, column=2, sticky="WE")
        okButton.grid(row=4, column=2, sticky="W")

        # chovani pri pokusu o zavreni okna pres "x" (lze zakazat)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # predek neziska fokus
        self.grab_set()

        # implicitni chovani klaves Return/Enter a Escape
        self.bind("<Return>", lambda event: self.ok())
        self.bind("<Escape>", lambda event: self.destroy())

        # ziskani fokusu
        self.entryFirstName.focus_set()

    def ok(self):
        print("first name:", self.entryFirstName.get())
        print("surname:", self.entrySurname.get())
        self.destroy()


root = tkinter.Tk()

showDialogButton = tkinter.Button(
    root, text="Show dialog", command=lambda: Dialog(root)
)

quitButton = tkinter.Button(root, text="Exit", command=exit)

showDialogButton.pack(fill=tkinter.BOTH)

tkinter.Label(text="").pack()

quitButton.pack(fill=tkinter.BOTH)

root.mainloop()
