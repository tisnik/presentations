#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "You type:\n{name}\n{surname}\n{age}".format(
            name=app.getEntry("name"),
            surname=app.getEntry("surname"),
            age=app.getEntry("age"))
        app.infoBox("You type:", msg)


def onTextChange(widgetName):
    if not app.getEntry(widgetName):
        app.setEntryInvalid(widgetName)
    else:
        app.setEntryValid(widgetName)


app = gui()

app.setSticky("news")
app.setPadding(2, 2)

app.addLabel("NameLbl", "Name:", 0, 0)
app.addValidationEntry("name", 0, 1, colspan=2)
app.setEntryMaxLength("name", 10)
app.setEntryWaitingValidation("name")
app.setEntryChangeFunction("name", onTextChange)

app.addLabel("SurnameLbl", "Surname:", 1, 0)
app.addValidationEntry("surname", 1, 1, colspan=2)
app.setEntryMaxLength("surname", 10)
app.setEntryWaitingValidation("surname")
app.setEntryChangeFunction("surname", onTextChange)

app.addLabel("AgeLbl", "Age:", 2, 0)
app.addNumericEntry("age", 2, 1, colspan=2)

app.addHorizontalSeparator(4, 0, colspan=3)

app.addButton("Show input", onButtonPress, 5, 1)
app.addButton("Quit", onButtonPress, 5, 2)

app.go()
