#!/usr/bin/env python

import tkinter
import turtle

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


app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

canvas = tkinter.Canvas(app.topLevel, width=600, height=600)
canvas.pack()

t, screen = setupTurtle(canvas)

t.hideturtle()
t.speed(0)
t.pencolor("green")

t.home()
t.pd()

screen.colormode(255)

r = 0
g = 0
b = 0
rd = 1

for i in range(72):
    t.left(5)
    for j in range(10):
        t.left(36)
        t.forward(80)
        for k in range(3):
            r += rd
            if r > 255 or r < 0:
                b += 10
                g += 10
                rd = -rd
                r += rd
            t.pencolor((r, g, b))
            t.forward(30)
            t.left(120)

screen.update()

app.go()
