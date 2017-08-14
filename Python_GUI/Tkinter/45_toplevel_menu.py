#!/usr/bin/env python

import tkinter
from tkinter import ttk


def test():
    print("Test!")


root = tkinter.Tk()

menubar = tkinter.Menu(root)
menubar.add_command(label="Test", command=test)
menubar.add_command(label="Quit", command=root.quit)

root.config(menu=menubar)

root.mainloop()
