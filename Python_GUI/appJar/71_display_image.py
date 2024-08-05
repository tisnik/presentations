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

app.addImage("image", "moare.png")

app.go()
