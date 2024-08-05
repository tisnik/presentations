#!/usr/bin/env python

import tkinter
import turtle
from math import *

from appJar import gui

app = gui()


def setupTurtle(canvas):
    screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle(screen)
    screen.tracer(100, 0)

    t.hideturtle()
    t.speed(0)

    t.home()
    t.pd()
    return t, screen


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


def drawFresnel():
    global progressBarValue

    x = 0.0
    y = 0.0
    f = 0.0

    for i in range(maxiter + 1):
        progressBarValue = 100.0 * i / maxiter
        f += fstep
        x += cos(f * f)
        y += sin(f * f)
        t.goto(scale * x, scale * y)

    screen.update()


def updateMeter():
    app.setMeter("progressBar", progressBarValue)


def onFresnelDraw(command):
    t.home()
    t.clear()
    drawFresnel()


def onMaxiterChange(widgetName):
    global maxiter
    value = app.getScale(widgetName)
    maxiter = int(value)


def onScaleChange(widgetName):
    global scale
    value = app.getScale(widgetName)
    scale = float(value)


def onFValueChange(widgetName):
    global fstep
    value = app.getScale(widgetName)
    fstep = float(value) / 100.0


def createGui(app):
    fileMenu = ["Quit"]

    app.addMenuList("File", fileMenu, onMenuItemSelect)

    app.addLabel("maxiter-label", "Maxiter", row=0, column=0)
    app.addScale("maxiter", row=0, column=1, colspan=2)
    app.showScaleIntervals("maxiter", 1000)
    app.showScaleValue("maxiter")
    app.setScaleRange("maxiter", 0, 5000, 1000)
    app.setScaleChangeFunction("maxiter", onMaxiterChange)

    app.addLabel("scale-label", "Scale", row=1, column=0)
    app.addScale("scale", row=1, column=1, colspan=2)
    app.showScaleIntervals("scale", 1)
    app.showScaleValue("scale")
    app.setScaleRange("scale", 1, 10, 4)
    app.setScaleChangeFunction("scale", onScaleChange)

    app.addLabel("f-value-label", "F-value", row=2, column=0)
    app.addScale("f-value", row=2, column=1, colspan=2)
    app.showScaleIntervals("f-value", 10)
    app.showScaleValue("f-value")
    app.setScaleRange("f-value", 0, 100, 20)
    app.setScaleChangeFunction("f-value", onFValueChange)

    app.addMeter("progressBar", row=3, column=0, colspan=2)
    app.setMeterFill("progressBar", "green")

    app.addButton("Draw", onFresnelDraw, row=3, column=2)

    app.registerEvent(updateMeter)


progressBarValue = 0
scale = 4.0
maxiter = 1000
fstep = 0.2

app.setSticky("news")

createGui(app)

canvas = tkinter.Canvas(app.topLevel, width=500, height=500)
canvas.pack()
t, screen = setupTurtle(canvas)

app.go()
