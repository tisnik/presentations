#!/usr/bin/env python

from appJar import gui


def onLinkClick(link):
    print(link)
    app.stop()


app = gui()

app.addLabel("title", "Hello world!", colspan=2)

app.addLink("Quit", onLinkClick)

app.go()
