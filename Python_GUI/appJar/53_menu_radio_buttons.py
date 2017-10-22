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


def zoomFunction(zoom):
    print(zoom)
    app.setLabel("zoomLbl", "{z}\u00d7".format(z=zoom))


fileMenu = ["Open", "Save", "Close"]
helpMenu = ["About", "Help"]

app = gui()

app.setSticky("news")
app.setPadding(10, 2)

app.addMenuList("File", fileMenu, [none, none, closeItemSelected])

app.createMenu("Zoom")

for i in range(1, 10):
    app.addMenuRadioButton("Zoom", "zoom", "{i}\u00d7".format(i=i),
                           lambda item, i=i: zoomFunction(i))

app.createMenu("Config")

for i in range(5):
    app.addMenuCheckBox("Config", "Size 1{s}".format(s=i))

app.addMenuList("Help", helpMenu, [showHelpDialog, showAboutDialog])

app.addHorizontalSeparator(0, 1, colspan=2)

app.addLabel("Zoom", "zoom", 1, 1)
app.addLabel("zoomLbl", "1\u00d7", 1, 2)

app.setGeometry("250x80")
app.go()
