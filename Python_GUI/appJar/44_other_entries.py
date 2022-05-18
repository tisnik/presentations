#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "You type:\n{name}\n{surname}\n{age}".format(
            name=app.getEntry("name"),
            surname=app.getEntry("surname"),
            age=app.getEntry("age"),
        )
        app.infoBox("You type:", msg)


app = gui()

app.setSticky("news")
app.setPadding(2, 2)

app.addLabel("NameLbl", "Name:", 0, 0)
app.addValidationEntry("name", 0, 1, colspan=2)
app.setEntryMaxLength("name", 10)
app.setEntryDefault("name", "your name")
app.setEntryInvalid("name")
app.setFocus("name")

app.addLabel("SurnameLbl", "Surname:", 1, 0)
app.addValidationEntry("surname", 1, 1, colspan=2)
app.setEntryMaxLength("surname", 10)
app.setEntryDefault("surname", "your surname")
app.setEntryInvalid("surname")

app.addLabel("AgeLbl", "Age:", 2, 0)
app.addNumericEntry("age", 2, 1, colspan=2)

app.addHorizontalSeparator(4, 0, colspan=3)

app.addButton("Show input", onButtonPress, 5, 1)
app.addButton("Quit", onButtonPress, 5, 2)

app.go()
