#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "Your choice of scale: {s}".format(s=app.getScale("scale"))
        app.infoBox("Show scale:", msg)


def scaleCallback(widgetName):
    value = app.getScale(widgetName)
    app.setTitle("Scale: {v}".format(v=value))
    app.setMeter("progressBar", value)


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addSplitMeter("progressBar", 0, 0, colspan=2)
app.setMeterFill("progressBar", ["green", "yellow"])

app.addLabelScale("scale", colspan=2)
app.showScaleIntervals("scale", 25)
app.showScaleValue("scale")
app.setScaleChangeFunction("scale", scaleCallback)
app.setScaleRange("scale", 0, 100, 50)

app.addButton("Show scale value", onButtonPress, 2, 0)
app.addButton("Quit", onButtonPress, 2, 1)

app.go()
