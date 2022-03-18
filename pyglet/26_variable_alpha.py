#!/usr/bin/env python

import pyglet
from pyglet.gl import *
from pyglet.window import key

window = pyglet.window.Window(width=450, height=450, caption="Pyglet+OpenGL")


alpha = 0.5

keys = key.KeyStateHandler()
window.push_handlers(keys)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # barva pozadi obrazku
    glClearDepth(1.0)  # implicitni hloubka ulozena v pameti hloubky
    glPolygonMode(GL_FRONT, GL_FILL)  # nastaveni rezimu vykresleni vyplnenych sten
    glPolygonMode(GL_BACK, GL_FILL)  # jak pro predni tak pro zadni steny
    glDisable(GL_CULL_FACE)  # zadne hrany ani steny se nebudou odstranovat


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)  # viditelna oblast pres cele okno


def clear_buffers():
    glClear(GL_COLOR_BUFFER_BIT)  # vymazani vsech bitovych rovin barvoveho bufferu


def set_projection():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # nahrat jednotkovou matici


def draw_background_plane():
    border = 10
    glDisable(GL_BLEND)  # zakaz blendingu
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(border, border)
    glVertex2f(window.width - border, border)
    glVertex2f(window.width - border, window.height - border)
    glVertex2f(border, window.height - border)
    glEnd()


def draw_square_with_blending(x, y, sfactor, dfactor, alpha):
    glBlendFunc(sfactor, dfactor)
    glColor4f(1.0, 1.0, 0.0, alpha)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 40, y)
    glVertex2f(x + 40, y + 40)
    glVertex2f(x, y + 40)
    glEnd()


@window.event
def on_draw():
    global alpha

    clear_buffers()
    set_projection()
    draw_background_plane()

    if keys[key.LEFT]:
        alpha = alpha - 0.01
    if keys[key.RIGHT]:
        alpha = alpha + 0.01
    if keys[key.R]:
        alpha = 0.5

    window.set_caption("Alpha = %3.2f" % alpha)
    glEnable(GL_BLEND)
    sfactors = [
        GL_SRC_ALPHA,
        GL_ONE_MINUS_SRC_ALPHA,
        GL_DST_COLOR,
        GL_ONE_MINUS_DST_COLOR,
        GL_ZERO,
        GL_ONE,
    ]
    dfactors = [
        GL_SRC_ALPHA,
        GL_ONE_MINUS_SRC_ALPHA,
        GL_SRC_COLOR,
        GL_ONE_MINUS_SRC_COLOR,
        GL_ZERO,
        GL_ONE,
    ]

    for y in xrange(0, 6):
        sfactor = sfactors[y]
        for x in xrange(0, 6):
            dfactor = dfactors[x]
            draw_square_with_blending(50 + 60 * x, 50 + 60 * y, sfactor, dfactor, alpha)


pyglet.app.run()
