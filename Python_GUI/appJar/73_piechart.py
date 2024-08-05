#!/usr/bin/env python

import tkinter

from appJar import gui

app = gui()


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


data = {
    "ODS": 25,
    "CSSD": 15,
    "STAN": 6,
    "KSČM": 15,
    "Piráti": 22,
    "TOP 09": 7,
    "ANO": 78,
    "KDU-ČSL": 10,
    "SPD": 22,
}

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addPieChart("piechart", data)

app.go()
