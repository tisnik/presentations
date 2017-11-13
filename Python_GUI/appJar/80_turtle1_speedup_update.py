#!/usr/bin/env python

from appJar import gui
import tkinter
import turtle


app = gui()


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

canvas = tkinter.Canvas(app.topLevel, width=256, height=256)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
screen.tracer(100, 0)

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

screen.update()

app.go()
