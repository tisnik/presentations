#!/usr/bin/env python

import sys
import tkinter
import turtle
from random import random

from appJar import gui

app = gui()


ifs_systems = {
    "binary": (
        (0.500000, 0.000000, 0.000000, 0.500000, -2.563477, -0.000003, 0.333333),
        (0.500000, 0.000000, 0.000000, 0.500000, 2.436544, -0.000003, 0.333333),
        (0.000000, -0.500000, 0.500000, 0.000000, 4.873085, 7.563492, 0.333333),
    ),
    "coral": (
        (0.307692, -0.531469, -0.461538, -0.293706, 5.401953, 8.655175, 0.400000),
        (0.307692, -0.076923, 0.153846, -0.447552, -1.295248, 4.152990, 0.150000),
        (0.000000, 0.545455, 0.692308, -0.195804, -4.893637, 7.269794, 0.450000),
    ),
    "crystal": (
        (0.696970, -0.481061, -0.393939, -0.662879, 2.147003, 10.310288, 0.747826),
        (0.090909, -0.443182, 0.515152, -0.094697, 4.286558, 2.925762, 0.252174),
    ),
    "dragon": (
        (0.824074, 0.281482, -0.212346, 0.864198, -1.882290, -0.110607, 0.787473),
        (0.088272, 0.520988, -0.463889, -0.377778, 0.785360, 8.095795, 0.212527),
    ),
    "dragon2": (
        (0.824074, 0.281481, -0.212346, 0.864197, -1.772710, 0.137795, 0.771268),
        (-0.138580, 0.283951, -0.670062, -0.279012, 2.930991, 7.338924, 0.228732),
    ),
    "feather": (
        (0.870370, 0.074074, -0.115741, 0.851852, -1.278016, 0.070331, 0.798030),
        (-0.162037, -0.407407, 0.495370, 0.074074, 6.835726, 5.799174, 0.201970),
    ),
    "fern": (
        (0.850000, 0.040000, -0.040000, 0.850000, 0.000000, 1.600000, 0.850000),
        (0.200000, -0.260000, 0.230000, 0.220000, 0.000000, 1.600000, 0.070000),
        (-0.150000, 0.280000, 0.260000, 0.240000, 0.000000, 0.440000, 0.070000),
        (0.000000, 0.000000, 0.000000, 0.160000, 0.000000, 0.000000, 0.010000),
    ),
    "koch": (
        (0.307692, 0.000000, 0.000000, 0.294118, 4.119164, 1.604278, 0.151515),
        (0.192308, -0.205882, 0.653846, 0.088235, -0.688840, 5.978916, 0.253788),
        (0.192308, 0.205882, -0.653846, 0.088235, 0.668580, 5.962514, 0.253788),
        (0.307692, 0.000000, 0.000000, 0.294118, -4.136530, 1.604278, 0.151515),
        (0.384615, 0.000000, 0.000000, -0.294118, -0.007718, 2.941176, 1.000000),
    ),
    "spiral": (
        (0.787879, -0.424242, 0.242424, 0.859848, 1.758647, 1.408065, 0.895652),
        (-0.121212, 0.257576, 0.151515, 0.053030, -6.721654, 1.377236, 0.052174),
        (0.181818, -0.136364, 0.090909, 0.181818, 6.086107, 1.568035, 0.052174),
    ),
    "tree": (
        (0.000000, 0.000000, 0.000000, 0.500000, 0.000000, 0.000000, 0.050000),
        (0.420000, -0.420000, 0.420000, 0.420000, 0.000000, 0.200000, 0.400000),
        (0.420000, 0.420000, -0.420000, 0.420000, 0.000000, 0.200000, 0.400000),
        (0.100000, 0.000000, 0.000000, 0.100000, 0.000000, 0.200000, 0.150000),
    ),
    "triangle": (
        (0.500000, 0.000000, 0.000000, 0.500000, -0.500000, 0.000000, 0.333333),
        (0.500000, 0.000000, 0.000000, 0.500000, 0.500000, 0.000000, 0.333333),
        (0.500000, 0.000000, 0.000000, 0.500000, 0.000000, 0.860000, 0.333334),
    ),
}


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

    dy = 100

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
            x2 = x1 * 30
            y2 = y1 * 30 - dy
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

    ifsMenu = sorted(ifs_systems.keys())
    for ifsMenuItem in ifsMenu:
        app.addMenuRadioButton(
            "IFS",
            "ifs",
            ifsMenuItem,
            lambda i, ifsMenuItem=ifsMenuItem: onIFSItemSelect(ifsMenuItem),
        )

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
ifs = ifs_systems["binary"]

app.setSticky("news")

createGui(app)

canvas = tkinter.Canvas(app.topLevel, width=500, height=500)
canvas.pack()
t, screen = setupTurtle(canvas)

app.go()
