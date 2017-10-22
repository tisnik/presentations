#!/usr/bin/env python

from appJar import gui


def showAboutDialog():
    app.infoBox("About", "App1")


def showHelpDialog():
    app.infoBox("Help", "simple\nhelp\nmessage")


def reallyQuit():
    return app.yesNoBox("Really quit?", "Really you really want to quit?")


def onMenuItemSelect(menuItem):
    if menuItem == "Close":
        if reallyQuit():
            app.stop()
    elif menuItem == "About":
        showAboutDialog()
    elif menuItem == "Help":
        showHelpDialog()


def onToolbarButtonPress(buttonName):
    if buttonName == "Off":
        if reallyQuit():
            app.stop()
    elif buttonName == "About":
        showAboutDialog()
    else:
        showHelpDialog()


tools = ["About", "Help", "Off"]

fileMenu = ["Open", "Save", "-", "Close"]
helpMenu = ["About", "Help"]

app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addToolbar(tools, onToolbarButtonPress, findIcon=True)
app.addMenuList("File", fileMenu, onMenuItemSelect)
app.addMenuList("Help", helpMenu, onMenuItemSelect)

app.setToolbarImage("Off", "icons/application-exit.gif")
app.setToolbarImage("About", "icons/about.png")
app.setToolbarImage("Help", "icons/help.png")

app.addHorizontalSeparator(0, 1, colspan=2)

app.go()
