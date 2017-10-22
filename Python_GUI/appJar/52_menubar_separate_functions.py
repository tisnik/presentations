#!/usr/bin/env python

from appJar import gui


def showAboutDialog(menuItem):
    app.infoBox("About", "App1")


def showHelpDialog(menuItem):
    app.infoBox("Help", "simple\nhelp\nmessage")


def reallyQuit():
    return app.yesNoBox("Really quit?", "Really you really want to quit?")


def none(menuItem):
    pass


def closeItemSelected(menuItem):
    if reallyQuit():
        app.stop()


fileMenu = ["Open", "Save", "Close"]
helpMenu = ["About", "Help"]

app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addMenuList("File", fileMenu, [none, none, closeItemSelected])
app.addMenuList("Help", helpMenu, [showHelpDialog, showAboutDialog])

app.addHorizontalSeparator(0, 1, colspan=2)

app.go()
