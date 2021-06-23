#!/usr/bin/env python

import pyglet
from pyglet.gl import *

window = pyglet.window.Window(width=600,
                              height=250,
                              caption="Pyglet library")

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load('gnome-globe.png', file=image_stream)
texture = image.get_texture()



def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)          # barva pozadi obrazku
    glPolygonMode(GL_FRONT, GL_FILL)          # nastaveni rezimu vykresleni modelu
    glPolygonMode(GL_BACK, GL_FILL)
    glDisable(GL_CULL_FACE)                   # zadne hrany ani steny se nebudou odstranovat

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glBindTexture(GL_TEXTURE_2D, texture.id)


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)           # viditelna oblast pres cele okno


def draw_quad(x, y):
    glBegin(GL_QUADS)

    glTexCoord2f(0.0, 0.0)
    glVertex2i(x, y)

    glTexCoord2f(1.0, 0.0)
    glVertex2i(x+150, y)

    glTexCoord2f(1.0, 1.0)
    glVertex2i(x+150, y+150)

    glTexCoord2f(0.0, 1.0)
    glVertex2i(x, y+150)

    glEnd()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)              # vymazani vsech bitovych rovin barvoveho bufferu
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 0.0)            # nastaveni mazaci barvy na cernou
    glClear(GL_COLOR_BUFFER_BIT)                # vymazani bitovych rovin barvoveho bufferu

    glEnable(GL_TEXTURE_2D)
    draw_quad(50, 50)

    glDisable(GL_TEXTURE_2D)
    draw_quad(210, 50)

    glEnable(GL_TEXTURE_2D)
    draw_quad(410, 50)


pyglet.app.run()
