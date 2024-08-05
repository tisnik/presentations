#!/usr/bin/env python

import tkinter

from appJar import gui

app = gui()


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

canvas = tkinter.Canvas(app.topLevel, width=256, height=256)
canvas.pack()

canvas.create_oval(10, 10, 100, 100, fill="red", outline="blue", width=3)
canvas.create_line(0, 0, 255, 255, width=5)
canvas.create_line(0, 255, 255, 0, dash=123)

canvas.create_rectangle(70, 140, 230, 180, fill="white")
canvas.create_text(150, 160, text="Hello world!", fill="brown", font="Helvetica 20")

app.go()
