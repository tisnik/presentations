#!/usr/bin/env python

from appJar import gui

CHECK_SYMBOL = "\u2713"
MULTIPLY_SYMBOL = "\u2715"


def state(choice):
    return CHECK_SYMBOL if choice else MULTIPLY_SYMBOL


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "1st choice: {c1}\n2nd choice: {c2}".format(
            c1=state(app.getCheckBox("1st choice")),
            c2=state(app.getCheckBox("2nd choice")),
        )
        app.infoBox("Show choices:", msg)


app = gui()

app.setSticky("news")
app.setPadding(10, 10)

app.addCheckBox("1st choice", 1, 1)
app.addCheckBox("2nd choice", 2, 1)

app.setCheckBox("1st choice", ticked=True)

app.addButton("Show choices", onButtonPress, 3, 1)
app.addButton("Quit", onButtonPress, 3, 2)

app.go()
