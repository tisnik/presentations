#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        app.infoBox("Ok, Ok", "Ok button pressed")


app = gui()

app.setSticky("news")
app.setPadding(10, 10)

app.addLabel("title", "Hello world!")

app.addButton("Ok", onButtonPress, 1, 1)
app.addButton("Quit", onButtonPress, 2, 1)

app.go()
