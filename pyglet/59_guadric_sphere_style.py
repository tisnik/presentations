#!/usr/bin/env python

import pyglet
from pyglet.gl import *
from pyglet.window import key

fov = 70.0  # zorny uhel (field of view)
nearPlane = 0.1  # blizsi orezavaci rovina
farPlane = 90.0  # vzdalenejsi orezavaci rovina

r1 = 0.0
r2 = 0.0

depthBufferEnabled = False  # povoleni ci zakaz Z-bufferu

quadricDrawStyle = GLU_LINE  # styl vykreslovani kvadriky
sphereSlices = 10  # rozdeleni koule na 'poledniky'
sphereStacks = 10  # rozdeleni koule na 'rovnobezky'


window = pyglet.window.Window(width=500, height=500, caption="Pyglet library")

keys = key.KeyStateHandler()


def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)  # barva pozadi obrazku
    glPolygonMode(GL_FRONT, GL_FILL)  # nastaveni rezimu vykresleni modelu
    glPolygonMode(GL_BACK, GL_FILL)

    # zakaz odstranovani hran nebo sten podle jejich normal
    glDisable(GL_CULL_FACE)
    glDepthFunc(GL_LESS)  # funkce pro testovani fragmentu

    glShadeModel(GL_SMOOTH)  # nastaveni stinovaciho rezimu
    glPointSize(3.0)


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)  # viditelna oblast pres cele okno


def draw_quadric(drawStyle, slices, stacks):
    radius = 8.0
    quadric = gluNewQuadric()  # vytvoreni kvadriky
    gluQuadricDrawStyle(quadric, drawStyle)  # nastaveni vlastnosti kvadriky
    gluQuadricNormals(quadric, GLU_SMOOTH)  # smer generovanych normal
    gluSphere(quadric, radius, slices, stacks)  # vykresleni kvadriky
    gluDeleteQuadric(quadric)  # zruseni kvadriky


def set_depth_buffer(depthBufferEnabled):
    if depthBufferEnabled:
        glEnable(GL_DEPTH_TEST)
    else:
        glDisable(GL_DEPTH_TEST)


def clear_buffers(depthBufferEnabled):
    if depthBufferEnabled:
        # vymazani vsech bitovych rovin barvoveho bufferu i Z bufferu
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    else:
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
def on_key_press(symbol, modifiers):
    global depthBufferEnabled
    global quadricDrawStyle
    global sphereSlices, sphereStacks

    if symbol == key.Z:
        depthBufferEnabled = not depthBufferEnabled
    if symbol == key.L:
        quadricDrawStyle = GLU_LINE
    if symbol == key.P:
        quadricDrawStyle = GLU_POINT
    if symbol == key.F:
        quadricDrawStyle = GLU_FILL
    if symbol == key.PAGEUP:
        sphereStacks += 1
    if symbol == key.PAGEDOWN:
        if sphereStacks > 1:
            sphereStacks -= 1
    if symbol == key.HOME:
        if sphereSlices > 1:
            sphereSlices -= 1
    if symbol == key.END:
        sphereSlices += 1


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

    clear_buffers(depthBufferEnabled)
    set_depth_buffer(depthBufferEnabled)
    set_projection_matrix(fov, nearPlane, farPlane)
    set_modelview_matrix(r1, r2)
    draw_quadric(quadricDrawStyle, sphereSlices, sphereStacks)


window.push_handlers(keys)
pyglet.app.run()
