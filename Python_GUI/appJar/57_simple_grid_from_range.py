#!/usr/bin/env python

from appJar import gui


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addGrid("grid", (range(1, 4), range(4, 7), range(7, 10), (" * ", " 0 ", " # ")))

app.go()
