#!/usr/bin/env python

from appJar import gui

meterValue = 50


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "Your choice of scale: {s}".format(s=app.getScale("scale"))
        app.infoBox("Show scale:", msg)


def scaleCallback(widgetName):
    global meterValue
    meterValue = app.getScale(widgetName)
    app.setTitle("Scale: {v}".format(v=meterValue))


def updateMeter():
    app.setMeter("progressBar", meterValue)


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addMeter("progressBar", 0, 0, colspan=2)
app.setMeterFill("progressBar", "green")

app.addLabelScale("scale", colspan=2)
app.showScaleIntervals("scale", 25)
app.showScaleValue("scale")
app.setScaleChangeFunction("scale", scaleCallback)
app.setScaleRange("scale", 0, 100, meterValue)

app.registerEvent(updateMeter)

app.addButton("Show scale value", onButtonPress, 2, 0)
app.addButton("Quit", onButtonPress, 2, 1)

app.go()
