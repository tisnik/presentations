#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        app.infoBox("Ok, Ok", "Ok button pressed")


app = gui()

app.setSticky("we")

app.addLabel("title", "Hello world!", colspan=2)

app.addButtons(["Ok", "Quit"], onButtonPress, 1, 0)

app.go()
