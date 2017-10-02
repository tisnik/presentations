#!/usr/bin/env python

from appJar import gui

app = gui()

app.setSticky("we")

app.addLabel("title", "Hello world!", colspan=2)

app.addButton("Ok", None, row=1, column=0)
app.addButton("Quit", None, row=1, column=1)

app.go()
