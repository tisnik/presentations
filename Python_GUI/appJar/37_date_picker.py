#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()


def showDate(btn):
    msg = "Selected date: {d}".format(d=app.getDatePicker("datePicker"))
    app.infoBox("Show scale:", msg)


app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addDatePicker("datePicker")
app.setDatePickerRange("datePicker", 2000, 2017)

app.addButton("Show selected date", showDate, 2, 0)
app.addButton("Quit", onButtonPress, 2, 1)

app.go()
