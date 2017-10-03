#!/usr/bin/env python

from appJar import gui


def onQuitButtonPress(buttonName):
    app.stop()


def onOkButtonPress(buttonName):
    app.infoBox("Ok, Ok", "Ok button pressed")


app = gui()

app.setSticky("we")

app.addLabel("title", "Hello world!", colspan=2)

app.addButtons(["Ok", "Quit"], [onOkButtonPress, onQuitButtonPress], 1, 0)

app.go()
