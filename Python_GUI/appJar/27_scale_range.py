#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "Your choice of scale: {s}".format(s=app.getScale("scale"))
        app.infoBox("Show scale:", msg)


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addLabelScale("scale", colspan=2)
app.showScaleIntervals("scale", 25)
app.showScaleValue("scale")
app.setScaleRange("scale", 50, 150, 100)

app.addButton("Show scale value", onButtonPress, 1, 0)
app.addButton("Quit", onButtonPress, 1, 1)

app.go()
