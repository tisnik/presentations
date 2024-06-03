#!/usr/bin/env python

from appJar import gui
import math
import tkinter
import turtle


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


def onDrawMenuSelect(menuItem):
    allParams = {
        "Tree": (-50, -150, 100, 45),
        "Bush": (40, -100, 80, 35),
        "Spiral": (-200, -150, 50, 70),
        "Spiral2": (-220, -50, 40, 80),
        "Spiral3": (-300, -50, 30, 85),
    }

    params = allParams[menuItem]

    t.hideturtle()
    t.speed(0)
    t.pencolor("gray")

    t.goto(params[0], params[1])
    t.pd()
    t.clear()

    house(params[2], params[3])
    screen.update()


def house(side, angle):
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
        t.right(90 - angle)
        # původní příkaz: domek side/sqrt 2 :uhel
        house(side * math.cos(math.radians(angle)), angle)
        # druhá část střechy
        t.right(90)
        # původní příkaz: domek side/sqrt 2 :uhel
        house(side * math.sin(math.radians(angle)), angle)
        # zbývající stěna
        t.right(angle)
        t.forward(side)
        t.left(90)
    else:
        t.forward(side)


app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

drawMenu = ["Tree", "Bush", "Spiral", "Spiral2", "Spiral3"]
app.addMenuList("Draw", drawMenu, onDrawMenuSelect)

canvas = tkinter.Canvas(app.topLevel, width=600, height=600)
canvas.pack()

t, screen = setupTurtle(canvas)

app.go()
