#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    if buttonName == "Quit":
        app.stop()
    else:
        msg = "You type: {login} + {password}".format(
            login=app.getEntry("login"), password=app.getEntry("password")
        )
        app.infoBox("You type:", msg)


app = gui()

app.setSticky("news")
app.setPadding(2, 2)

app.addLabel("LoginLbl", "Login:", 0, 0)
app.addEntry("login", 0, 1, colspan=2)
app.setEntryMaxLength("login", 8)
app.setEntryDefault("login", "your login")

app.addLabel("PasswordLbl", "Password:", 1, 0)
app.addSecretEntry("password", 1, 1, colspan=2)

app.addHorizontalSeparator(2, 0, colspan=3)

app.addButton("Show input", onButtonPress, 3, 1)
app.addButton("Quit", onButtonPress, 3, 2)

app.go()
