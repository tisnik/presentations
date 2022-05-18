#!/usr/bin/env python

from appJar import gui


def showAboutDialog():
    app.infoBox("About", "App1")


def showHelpDialog():
    app.infoBox("Help", "simple\nhelp\nmessage")


def showInfoDialog(buttonName):
    app.infoBox("Help", "You clicked on: " + buttonName)


def reallyQuit():
    return app.yesNoBox("Really quit?", "Really you really want to quit?")


def onToolbarButtonPress(buttonName):
    if buttonName == "Off":
        if reallyQuit():
            app.stop()
    elif buttonName == "About":
        showAboutDialog()
    elif buttonName == "Help":
        showHelpDialog()
    else:
        showInfoDialog(buttonName)


tools = [
    "About",
    "Alarm",
    "Computer",
    "Construction",
    "Refresh",
    "Open",
    "Close",
    "Save",
    "Display",
    "Files",
    "New",
    "Settings",
    "Print",
    "Printer",
    "Search",
    "Undo",
    "Redo",
    "Preferences",
    "Home",
    "Help",
    "Calendar",
    "Web",
    "Spaceship",
    "Wizard",
    "Off",
]

app = gui()

app.addToolbar(tools, onToolbarButtonPress, findIcon=True)

app.go()
