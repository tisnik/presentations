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


def spiral(t, color, angle, maxiter):
    t.home()
    t.clear()
    t.pencolor(color)
    side = 0

    for _ in range(maxiter):
        t.forward(side)
        t.right(angle)
        side += 1


def kochCurve(t, length, limit):
    if length > limit:
        kochCurve(t, length / 3, limit)
        t.right(60)
        kochCurve(t, length / 3, limit)
        t.left(120)
        kochCurve(t, length / 3, limit)
        t.right(60)
        kochCurve(t, length / 3, limit)
    else:
        t.forward(length)


def kochSnowflake(t, limit):
    t.home()
    t.goto(-70, -70)
    t.clear()
    t.pencolor("blue")

    for _ in range(3):
        kochCurve(t, 150, limit)
        t.left(120)


def pentagon(t):
    for _ in range(5):
        t.forward(70)
        t.right(72)


def wheel(t):
    t.home()
    t.clear()
    t.pencolor("brown")
    for _ in range(36):
        pentagon(t)
        t.left(10)


def onTurtleCommandSelect(command):
    if command == "Spiral 1":
        spiral(t, "green", 117, 160)
    elif command == "Spiral 2":
        spiral(t, "#404080", 119, 182)
    elif command == "Spiral 3":
        spiral(t, "#804040", 88, 200)
    elif command == "Koch snowflake 1":
        kochSnowflake(t, 20)
    elif command == "Koch snowflake 2":
        kochSnowflake(t, 10)
    elif command == "Koch snowflake 3":
        kochSnowflake(t, 5)
    elif command == "Wheel":
        wheel(t)
    screen.update()


app.setSticky("news")

fileMenu = ["Quit"]
turtleMenu = [
    "Spiral 1",
    "Spiral 2",
    "Spiral 3",
    "Koch snowflake 1",
    "Koch snowflake 2",
    "Koch snowflake 3",
    "Wheel",
]
app.addMenuList("File", fileMenu, onMenuItemSelect)
app.addMenuList("Turtle", turtleMenu, onTurtleCommandSelect)

canvas = tkinter.Canvas(app.topLevel, width=256, height=256)
canvas.pack()

t, screen = setupTurtle(canvas)

app.go()
