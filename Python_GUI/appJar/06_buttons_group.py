#!/usr/bin/env python

from appJar import gui

app = gui()

app.setSticky("we")

app.addLabel("title", "Hello world!", colspan=2)

app.addButtons(["Ok", "Quit"], None, 1, 0)

app.go()
