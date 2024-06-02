#!/usr/bin/env python

from appJar import gui
import tkinter
import turtle
from math import *


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


def kochCurve(t, length, iter):
    if iter > 1:
        kochCurve(t, length / 3, iter - 1)
        t.right(60)
        kochCurve(t, length / 3, iter - 1)
        t.left(120)
        kochCurve(t, length / 3, iter - 1)
        t.right(60)
        kochCurve(t, length / 3, iter - 1)
    else:
        t.forward(length)


def kochSnowflake(t, iter):
    for _ in range(3):
        kochCurve(t, 200, iter)
        t.left(120)


def prepareTurtle(t):
    t.home()
    t.goto(-100, -60)
    t.clear()


def onKochSnowflakeSelect(command):
    prepareTurtle(t)
    t.pencolor("blue")

    iter = int(command[0])
    kochSnowflake(t, iter)
    screen.update()


def onKochCombinationSelect(command):
    prepareTurtle(t)

    colors = ["red", "orange", "blue", "brown"]
    for i in range(4):
        t.pencolor(colors[i])
        kochSnowflake(t, i + 1)

    screen.update()


app.setSticky("news")

fileMenu = ["Quit"]
kochMenu = [
    "1 iterarion",
    "2 iterations",
    "3 iterations",
    "4 iterations",
    "5 iterations",
]
specialMenu = ["Combine snowflakes"]

app.addMenuList("File", fileMenu, onMenuItemSelect)
app.addMenuList("Koch Snowflake", kochMenu, onKochSnowflakeSelect)
app.addMenuItem("Special", "Combine snowflakes", onKochCombinationSelect)

canvas = tkinter.Canvas(app.topLevel, width=256, height=256)
canvas.pack()

t, screen = setupTurtle(canvas)

app.go()
