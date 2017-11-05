#!/usr/bin/env python

from appJar import gui
import tkinter


app = gui()


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addImage("image", "moare.png")

app.go()
