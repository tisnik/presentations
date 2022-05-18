#!/usr/bin/env python

from appJar import gui


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


def onButtonPress(buttonName):
    cells = app.getGridSelectedCells("grid")
    print(cells)


def createTable(n):
    return [[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addGrid("grid", createTable(10))

app.addButton("Show selected cells", onButtonPress)

app.go()
