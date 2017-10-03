#!/usr/bin/env python

from appJar import gui


def onButtonPress(buttonName):
    app.stop()


app = gui()

app.setSticky("we")

app.addLabel("title", "Hello world!", colspan=2)

app.addLabel("redLabel", "Red")
app.addLabel("orangeLabel", "Orange")
app.addLabel("yellowLabel", "Yellow")
app.addLabel("greenLabel", "Green")
app.addLabel("blueLabel", "Blue")

app.setLabelBg("redLabel", "red")
app.setLabelBg("orangeLabel", "orange")
app.setLabelBg("yellowLabel", "yellow")
app.setLabelBg("greenLabel", "green")
app.setLabelBg("blueLabel", "blue")

app.addButton("Quit", onButtonPress)

app.go()
