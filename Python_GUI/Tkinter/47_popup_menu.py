#!/usr/bin/env python

import tkinter
from tkinter import ttk


def test():
    print("Test!")


root = tkinter.Tk()

popup = tkinter.Menu(root, tearoff=0)

popup.add_command(label="Open")
popup.add_command(label="Save")
popup.add_separator()
popup.add_command(label="Exit", command=root.quit)


def on_popup(event):
    popup.post(event.x_root-5, event.y_root-5)


root.bind("<Button-3>", on_popup)
root.mainloop()
