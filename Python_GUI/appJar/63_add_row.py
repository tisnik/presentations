#!/usr/bin/env python

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


def onAddRow(data):
    if data == "newRow":
        values = app.getGridEntries("grid")
        print(values)
        if values[0] and values[1]:
            app.addGridRow("grid", values)


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

table = [["Name", "Work hours"],
         ["Petr", 160],
         ["Pavel", 90],
         ["Honza", 120]]

app.addGrid("grid", table, action=onAddRow, addRow=True)

app.addButton("Show selected cells", onButtonPress)

app.go()
