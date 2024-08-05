#!/usr/bin/env python

import re

from appJar import gui

treeContent = """
<html>
    <head>
        <title>Titulek</title>
    </head>
    <body>
        <h1>Kapitola</h1>
        <div>První odstavec</div>
        <div>Druhý odstavec</div>
        <div>Třetí odstavec</div>
    </body>
</html>
"""


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


def onButtonPress(buttonName):
    item = app.getTreeSelected("tree")
    if item is None:
        app.warningBox("Warning", "No item (node) selected")
    else:
        app.infoBox("Selected item", item)


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addTree("tree", treeContent)
app.setTreeEditable("tree", True)

app.addButton("Show selected item", onButtonPress)

app.go()
