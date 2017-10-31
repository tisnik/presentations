#!/usr/bin/env python

from appJar import gui


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addGrid("grid",
            [['', '', ''],
             [' 1 ', ' 2 ', ' 3 '],
             [' 4 ', ' 5 ', ' 6 '],
             [' 7 ', ' 8 ', ' 9 '],
             [' * ', ' 0 ', ' # ']])

app.go()
