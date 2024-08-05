#!/usr/bin/env python

import re

from appJar import gui


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


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


def showWorkHours(values):
    name = values[0]
    hours = int(values[1])
    norm = 160
    utilization = 100.0 * hours / norm
    message = "{h} of {n} hours: {u:.0f} %".format(h=hours, n=norm, u=utilization)
    app.infoBox("Work hours for " + name, message)


def addNewRow(values):
    values = app.getGridEntries("grid")
    print(values)
    if values[0] and values[1] and re.search("\d", values[1]):
        app.addGridRow("grid", values)


def onAddRow(data):
    if data == "newRow":
        addNewRow(data)
    else:
        showWorkHours(data)


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

table = [["Name", "Work hours"], ["Petr", 160], ["Pavel", 90], ["Honza", 120]]

app.addGrid("grid", table, action=onAddRow, addRow=True)

app.addButton("Show selected cells", onButtonPress)

app.go()
