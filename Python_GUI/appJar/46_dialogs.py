#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Info":
        app.infoBox("Info box", "Info box")
    elif buttonName == "Error":
        app.errorBox("Error box", "Error box")
    elif buttonName == "Warning":
        app.warningBox("Warning box", "Warning box")
    else:
        app.stop()


app = gui()

app.addButtons(["Info", "Error", "Warning", "Quit"], onButtonPress)

app.go()
