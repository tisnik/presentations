#!/usr/bin/env python

from appJar import gui
import tkinter


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app = gui()

app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addMicroBit("microbit")

for y in range(0, 5):
    for x in range(0, 5):
        brightness = x + y + 1
        app.setMicroBitPixel("microbit", x, y, brightness)

app.go()
