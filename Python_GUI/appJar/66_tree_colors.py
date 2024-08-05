#!/usr/bin/env python

import re

from appJar import gui

treeContent = """
<html>
    <head>
        <title>Titulek</title>
    </head>
    <body>
        <div>První odstavec</div>
        <div>Druhý odstavec</div>
        <div>Třetí odstavec</div>
    </body>
</html>
"""


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addTree("tree", treeContent)
app.setTreeEditable("tree", False)
app.setTreeColours("tree", "black", "#aaffaa", "red", "yellow")

app.go()
