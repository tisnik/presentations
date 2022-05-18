#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "Your choices: {c}".format(c=app.getProperties("properties"))
        app.infoBox("Show choices:", msg)


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addProperties(
    "properties",
    {"Assembler": True, "C": True, "C++": False, "Perl": False, "Python": True},
)

app.addButton("Show choice", onButtonPress)
app.addButton("Quit", onButtonPress)

app.go()
