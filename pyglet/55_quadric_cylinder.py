#!/usr/bin/env python

import pyglet
from pyglet.gl import *
from pyglet.window import key

fov = 70.0  # zorny uhel (field of view)
nearPlane = 0.1  # blizsi orezavaci rovina
farPlane = 90.0  # vzdalenejsi orezavaci rovina

r1 = 0.0
r2 = 0.0


window = pyglet.window.Window(width=500, height=500, caption="Pyglet library")

keys = key.KeyStateHandler()
window.push_handlers(keys)


def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)  # barva pozadi obrazku
    glPolygonMode(GL_FRONT, GL_FILL)  # nastaveni rezimu vykresleni modelu
    glPolygonMode(GL_BACK, GL_FILL)

    # zakaz odstranovani hran nebo sten podle jejich normal
    glDisable(GL_CULL_FACE)

    glShadeModel(GL_SMOOTH)  # nastaveni stinovaciho rezimu


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)  # viditelna oblast pres cele okno


def draw_quadric():
    baseRadius = 8.0
    topRadius = 8.0
    height = 10.0
    slices = 50
    stacks = 10
    quadric = gluNewQuadric()  # vytvoreni kvadriky
    gluQuadricDrawStyle(quadric, GLU_LINE)  # nastaveni vlastnosti kvadriky
    gluQuadricNormals(quadric, GLU_SMOOTH)  # smer generovanych normal
    glTranslatef(0, 0, -height / 2)  # vycentrovani valce
    gluCylinder(quadric, baseRadius, topRadius, height, slices, stacks)
    gluDeleteQuadric(quadric)  # zruseni kvadriky


def clear_buffers():
    # vymazani vsech bitovych rovin barvoveho bufferu
    glClear(GL_COLOR_BUFFER_BIT)


def set_projection_matrix(fov, nearPlane, farPlane):
    # zacatek modifikace projekcni matice
    glMatrixMode(GL_PROJECTION)
    # vymazani projekcni matice (=identita)
    glLoadIdentity()
    gluPerspective(fov, 1.0, nearPlane, farPlane)


def set_modelview_matrix(rotation1, rotation2):
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

    glRotatef(rotation1, 1.0, 0.0, 0.0)  # rotace objektu
    glRotatef(rotation2, 0.0, 1.0, 0.0)


@window.event
def on_draw():
    global r1, r2

    if keys[key.LEFT]:
        r2 -= 2
    if keys[key.RIGHT]:
        r2 += 2
    if keys[key.UP]:
        r1 -= 2
    if keys[key.DOWN]:
        r1 += 2

    clear_buffers()
    set_projection_matrix(fov, nearPlane, farPlane)
    set_modelview_matrix(r1, r2)
    draw_quadric()  # vykresleni dratoveho modelu valce


pyglet.app.run()
