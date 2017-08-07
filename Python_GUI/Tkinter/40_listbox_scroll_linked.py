#!/usr/bin/env python

import tkinter
from tkinter import ttk

import sys

root = tkinter.Tk()

scrollbar = ttk.Scrollbar(root)

langs = ("Assembler", "Basic", "Brainfuck", "C", "C++", "Java", "Julia",
         "Perl", "Python")

listbox = tkinter.Listbox(root, yscrollcommand=scrollbar.set, height=4)

scrollbar.config(command=listbox.yview)


for lang in langs:
    listbox.insert(tkinter.END, lang)


def on_listbox_select(event):
    index = listbox.curselection()[0]
    global langs
    print(langs[index])


listbox.bind("<<ListboxSelect>>", on_listbox_select)

quitButton = ttk.Button(root, text="Exit", command=exit)

listbox.grid(column=1, row=1, sticky="nswe")
scrollbar.grid(column=2, row=1, sticky="ns")
quitButton.grid(column=1, row=2)

root.mainloop()
