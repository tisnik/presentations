#!/usr/bin/env python

from appJar import gui


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


def parseCellAddress(cell):
    a = cell.split("-")
    return (int(a[0]), int(a[1]))


def onButtonPress(buttonName):
    cells = app.getGridSelectedCells("grid")
    selectedCells = [c for c, v in cells.items() if v]
    selectedCells.sort()
    print(selectedCells)
    if selectedCells:
        message = " ".join(selectedCells)
        app.infoBox("Selected cells", message)
    else:
        app.warningBox("Warning", "Please select at least one cell")
    addresses = [parseCellAddress(c) for c in selectedCells]
    print(addresses)


def createTable(n):
    return [[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addGrid("grid", createTable(10))

app.addButton("Show selected cells", onButtonPress)

app.go()
