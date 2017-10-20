#!/usr/bin/env python

from appJar import gui


def reallyQuit():
    return app.yesNoBox("Really quit?", "Really you really want to quit?")


def onButtonPress(buttonName):
    if buttonName == "Yes/No":
        print(app.yesNoBox("Yes No box", "Yes No box"))
    elif buttonName == "Ok/Cancel":
        print(app.okBox("Ok/Cancel box", "Ok/Cancel box"))
    elif buttonName == "Retry/Cancel":
        print(app.retryBox("Retry/Cancel box", "Retry/Cancel box"))
    else:
        if reallyQuit():
            app.stop()


app = gui()

app.addButtons(["Yes/No", "Ok/Cancel", "Retry/Cancel", "Quit"], onButtonPress)

app.go()
