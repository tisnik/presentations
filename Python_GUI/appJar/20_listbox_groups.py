#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "Your choices: {c}".format(c=app.getListItems("listbox"))
        app.infoBox("Show choices:", msg)


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addListBox("listbox", ["Assembler", "C", "C++", "Perl", "Python"])
app.setListBoxMulti("listbox", True)

app.addButton("Show choice", onButtonPress)
app.addButton("Quit", onButtonPress)

app.go()
