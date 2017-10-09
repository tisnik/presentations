#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "Your choice: {c}".format(c=app.getRadioButton("languages"))
        app.infoBox("Show choices:", msg)


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addRadioButton("languages", "Assembler", 1, 1)
app.addRadioButton("languages", "C", 2, 1)
app.addRadioButton("languages", "C++", 3, 1)
app.addRadioButton("languages", "Perl", 4, 1)
app.addRadioButton("languages", "Python", 5, 1)

app.setRadioButton("languages", "Python")

app.addButton("Show choice", onButtonPress, 6, 1)
app.addButton("Quit", onButtonPress, 6, 2)

app.go()
