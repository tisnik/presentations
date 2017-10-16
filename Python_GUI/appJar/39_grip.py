#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addLabel("topLabel", "\u25bc", 0, 1)
app.addLabel("leftLabel", "grip \u25b6", 1, 0)
app.addLabel("rightLabel", "\u25c0 grip", 1, 2)
app.addLabel("bottomLabel", "\u25b2", 2, 1)
app.addGrip(1, 1)

app.addButton("Quit", onButtonPress, 4, 1)

app.go()
