#!/usr/bin/env python

import tkinter
import turtle

from appJar import gui

app = gui()


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

canvas = tkinter.Canvas(app.topLevel, width=256, height=256)
canvas.pack()

t = turtle.RawTurtle(canvas)

t.hideturtle()
t.speed(0)
t.pencolor("green")

t.home()
t.pd()

side = 0
angle = 117

for _ in range(160):
    t.forward(side)
    t.right(angle)
    side += 1

app.go()
