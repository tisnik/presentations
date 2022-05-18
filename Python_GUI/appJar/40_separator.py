#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "Your choice of scales:\n{s1}\n{s2}".format(
            s1=app.getScale("scale1"), s2=app.getScale("scale2")
        )
        app.infoBox("Show scale:", msg)


def scaleCallback(widgetName):
    value1 = app.getScale("scale1")
    value2 = app.getScale("scale2")
    app.setMeter("progressBar", [value1, value2])


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addDualMeter("progressBar", 0, 1, colspan=2)
app.setMeterFill("progressBar", ["yellow", "red"])

app.addHorizontalSeparator(1, 1, colspan=2, colour="blue")

app.addVerticalSeparator(0, 0, rowspan=6)
app.addVerticalSeparator(0, 3, rowspan=6)

app.addLabelScale("scale1", 2, 1, colspan=2)
app.showScaleIntervals("scale1", 25)
app.showScaleValue("scale1")

app.addLabelScale("scale2", 3, 1, colspan=2)
app.showScaleIntervals("scale2", 25)
app.showScaleValue("scale2")

app.addHorizontalSeparator(4, 1, colspan=2, colour="green")

app.setScaleChangeFunction("scale1", scaleCallback)
app.setScaleChangeFunction("scale2", scaleCallback)

app.setScaleRange("scale1", 0, 100, 50)
app.setScaleRange("scale2", 0, 100, 50)

app.addButton("Show scale value", onButtonPress, 5, 1)
app.addButton("Quit", onButtonPress, 5, 2)

app.go()
