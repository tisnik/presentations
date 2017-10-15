#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addMeter("progressBar", 1, 0)
app.addButton("Quit", onButtonPress, 1, 1)

app.go()
