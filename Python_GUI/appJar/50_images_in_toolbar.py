#!/usr/bin/env python

from appJar import gui


def showAboutDialog():
    app.infoBox("About", "App1")


def showHelpDialog():
    app.infoBox("Help", "simple\nhelp\nmessage")


def reallyQuit():
    return app.yesNoBox("Really quit?", "Really you really want to quit?")


def onToolbarButtonPress(buttonName):
    if buttonName == "Off":
        if reallyQuit():
            app.stop()
    elif buttonName == "About":
        showAboutDialog()
    else:
        showHelpDialog()


tools = ["About", "Help", "Off"]

app = gui()

app.addToolbar(tools, onToolbarButtonPress, findIcon=True)

app.setToolbarImage("Off", "icons/application-exit.gif")
app.setToolbarImage("About", "icons/about.png")
app.setToolbarImage("Help", "icons/help.png")

app.go()
