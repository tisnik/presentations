#!/usr/bin/env python

import sys
import tkinter
import turtle
from random import random

from appJar import gui

app = gui()


ifs = (
    (+0.85000, +0.04000, -0.04000, +0.85000, +0.00000, +1.60000, +0.85000),
    (+0.20000, -0.26000, +0.23000, +0.22000, +0.00000, +1.60000, +0.07000),
    (-0.15000, +0.28000, +0.26000, +0.24000, +0.00000, +0.44000, +0.07000),
    (+0.00000, +0.00000, +0.00000, +0.16000, +0.00000, +0.00000, +0.01000),
)


def setupTurtle(canvas):
    screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle(screen)
    screen.tracer(100, 0)

    t.hideturtle()
    t.speed(0)

    t.home()
    t.pu()
    return t, screen


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


def onIFSItemSelect(menuItem):
    global ifs
    ifs = ifs_systems[menuItem]


def drawIFS(ifs):
    global progressBarValue
    start_iter = 100

    # generovane souradnice
    x1 = 0
    y1 = 0

    dy = 220
    scale = 45

    for i in range(maxiter + 1):
        progressBarValue = 100.0 * i / maxiter

        # nahodne vybrat transformaci
        pp = random()
        sum = 0
        k = 0
        while sum <= pp:
            sum += ifs[k][6]
            k += 1
        k -= 1

        # aplikovat transformaci
        x2 = x1 * ifs[k][0] + y1 * ifs[k][1] + ifs[k][4]
        y2 = x1 * ifs[k][2] + y1 * ifs[k][3] + ifs[k][5]
        x1 = x2
        y1 = y2

        # pokud byl prekrocen pocet startovnich iteraci
        if i > start_iter:
            x2 = x1 * scale
            y2 = y1 * scale - dy
            t.goto(x2, y2)
            t.dot(1)

    screen.update()


def updateMeter():
    app.setMeter("progressBar", progressBarValue)


def onIFSDraw(command):
    t.home()
    t.clear()
    drawIFS(ifs)


def onMaxiterChange(widgetName):
    global maxiter
    value = app.getScale(widgetName)
    maxiter = int(value)


def createGui(app):
    fileMenu = ["Quit"]

    app.addMenuList("File", fileMenu, onMenuItemSelect)

    app.addLabel("maxiter-label", "Maxiter", row=0, column=0)
    app.addScale("maxiter", row=0, column=1, colspan=2)
    app.showScaleIntervals("maxiter", 5000)
    app.showScaleValue("maxiter")
    app.setScaleRange("maxiter", 0, 25000, 5000)
    app.setScaleChangeFunction("maxiter", onMaxiterChange)

    app.addMeter("progressBar", row=3, column=0, colspan=2)
    app.setMeterFill("progressBar", "green")

    app.addButton("Draw", onIFSDraw, row=3, column=2)

    app.registerEvent(updateMeter)


progressBarValue = 0
maxiter = 5000

app.setSticky("news")

createGui(app)

canvas = tkinter.Canvas(app.topLevel, width=500, height=500)
canvas.pack()
t, screen = setupTurtle(canvas)

app.go()
