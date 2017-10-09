#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "Your choice: {c}".format(c=app.getOptionBox("optionbox"))
        app.infoBox("Show choices:", msg)


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addTickOptionBox("optionbox", ["Assembler", "C", "C++", "Perl", "Python"])

app.addButton("Show choice", onButtonPress)
app.addButton("Quit", onButtonPress)

app.go()
