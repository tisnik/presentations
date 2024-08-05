#!/usr/bin/env python

import math
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


def house(side):
    if side > 4:
        # základna
        t.forward(side)
        # úhlopříčka
        t.left(90 + 45)
        t.forward(side * math.sqrt(2))
        # stěna
        t.left(90 + 45)
        t.forward(side)
        # úhlopříčka
        t.left(90 + 45)
        t.forward(side * math.sqrt(2))
        # úsečka pod střechou
        t.left(90 + 45)
        t.forward(side)
        # první část střechy
        t.right(90)
        t.right(90 - 45)
        # původní příkaz: domek side/sqrt 2 :uhel
        house(side * math.cos(math.radians(45)))
        # druhá část střechy
        t.right(90)
        # původní příkaz: domek side/sqrt 2 :uhel
        house(side * math.sin(math.radians(45)))
        # zbývající stěna
        t.right(45)
        t.forward(side)
        t.left(90)
    else:
        t.forward(side)


app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

canvas = tkinter.Canvas(app.topLevel, width=600, height=600)
canvas.pack()

t, screen = setupTurtle(canvas)
t.goto(-50, -150)
t.clear()
house(100)
screen.update()

app.go()
