#!/usr/bin/env python

import pyglet
from pyglet.gl import *
from pyglet.window import key

fov = 70.0  # hodnota zorneho uhlu - field of view
nearPlane = 0.1  # blizsi orezavaci rovina
farPlane = 90.0  # vzdalenejsi orezavaci rovina

r1 = 0.0
r2 = 0.0

window = pyglet.window.Window(width=500, height=500, caption="Pyglet+OpenGL")


keys = key.KeyStateHandler()
window.push_handlers(keys)


def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)  # barva pozadi obrazku
    glPolygonMode(GL_FRONT, GL_FILL)  # nastaveni rezimu vykresleni vyplnenych sten
    glPolygonMode(GL_BACK, GL_FILL)  # jak pro predni tak pro zadni steny
    glDisable(GL_CULL_FACE)  # zadne hrany ani steny se nebudou odstranovat


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)  # viditelna oblast pres cele okno


@window.event
def on_draw():
    global r1, r2

    if keys[key.LEFT]:
        r2 = r2 - 1
    if keys[key.RIGHT]:
        r2 = r2 + 1
    if keys[key.UP]:
        r1 = r1 - 1
    if keys[key.DOWN]:
        r1 = r1 + 1

    glClear(GL_COLOR_BUFFER_BIT)  # vymazani vsech bitovych rovin barvoveho bufferu

    glMatrixMode(GL_PROJECTION)  # zacatek modifikace projekcni matice
    glLoadIdentity()  # vymazani projekcni matice (=identita)
    gluPerspective(fov, 1.0, nearPlane, farPlane)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # nahrat jednotkovou matici

    gluLookAt(
        4.0,
        6.0,
        18.0,  # bod, odkud se kamera diva
        0.0,
        2.0,
        0.0,  # bod, kam se kamera diva
        0.0,
        1.0,
        0.0,
    )  # poloha "stropu" ve scene

    glRotatef(r1, 1.0, 0.0, 0.0)  # rotace objektu
    glRotatef(r2, 0.0, 1.0, 0.0)

    glBegin(GL_QUADS)  # vykresleni otevrene krychle - sten domecku
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-5.0, -5.0, -5.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glVertex3f(5.0, -5.0, 5.0)
    glVertex3f(5.0, -5.0, -5.0)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, -5.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-5.0, -5.0, -5.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, -5.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(5.0, -5.0, -5.0)
    glVertex3f(5.0, -5.0, 5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, -5.0)
    glEnd()

    glBegin(GL_TRIANGLES)  # vykresleni strechy domecku z trojuhelniku
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(5.0, 5.0, -5.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(5.0, 5.0, -5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(0.0, 11.0, 0.0)
    glEnd()


pyglet.app.run()
