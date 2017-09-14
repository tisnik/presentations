#!/usr/bin/env python

import tkinter
from tkinter import ttk
import sys


def exit():
    sys.exit(0)


root = tkinter.Tk()

text = tkinter.Text(root,
                    font="Helvetica 20",
                    wrap=tkinter.WORD,
                    tabs="7c right 11c left",
                    width=40, height=16)

text.tag_configure("nadpis", foreground="red", underline=True)
text.tag_configure("suma", foreground="blue")

text.insert(tkinter.END, "Mesic\tObrat\n", "nadpis")
text.insert(tkinter.END, "leden\t100\n")
text.insert(tkinter.END, "unor\t200\n")
text.insert(tkinter.END, "brezen\t0\n")
text.insert(tkinter.END, "duben\t1000\n")
text.insert(tkinter.END, "kveten\t100\n")
text.insert(tkinter.END, "cerven\t200\n")
text.insert(tkinter.END, "cervenec\t0\tdovolene\n")
text.insert(tkinter.END, "srpen\t1000\n")
text.insert(tkinter.END, "zari\t100\n")
text.insert(tkinter.END, "rijen\t200\n")
text.insert(tkinter.END, "listopad\t0\n")
text.insert(tkinter.END, "prosinec\t1100\tvanoce\n\n")
text.insert(tkinter.END, "suma\t3900\n", "suma")

button = tkinter.Button(root, text="Close window", command=exit)

text.pack()
button.pack()

root.mainloop()
