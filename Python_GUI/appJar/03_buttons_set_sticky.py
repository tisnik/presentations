#!/usr/bin/env python

from appJar import gui

app = gui()

app.setSticky("we")

app.addLabel("title", "Hello world!")

app.addButton("Ok", None)
app.addButton("Quit", None)

app.go()
