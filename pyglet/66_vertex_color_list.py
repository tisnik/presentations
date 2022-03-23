#!/usr/bin/env python

import pyglet
from pyglet.gl import *
from pyglet.window import key

nearPlane = 0.1  # blizsi orezavaci rovina
farPlane = 90.0  # vzdalenejsi orezavaci rovina

window = pyglet.window.Window(width=500, height=500, caption="Pyglet library")

keys = key.KeyStateHandler()
window.push_handlers(keys)


def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)  # barva pozadi obrazku


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)  # viditelna oblast pres cele okno


def prepare_scene():
    # priprava seznamu vertexu
    # parametry:
    #     8   - pocet vertexu
    #     v2f - format: vertex se dvema souradnicemi typu 'float'
    #     ()  - n-tice s osmi vertexy (8x2 = 16 hodnot typu 'float')
    #     c3b - format: barva se tremi slozkami typu 'byte'
    #     ()  - n-tice s osmi barvami (8x3 = 24 hodnot typu 'byte')
    return pyglet.graphics.vertex_list(
        8,
        (
            "v2f",
            (
                -0.5,
                -0.5,
                -0.5,
                +0.5,
                +0.5,
                +0.5,
                +0.5,
                -0.5,
                +0.2,
                +0.2,
                -0.2,
                -0.2,
                -0.2,
                +0.2,
                +0.2,
                -0.2,
            ),
        ),
        (
            "c3B",
            (
                0xFF,
                0x00,
                0xFF,
                0xFF,
                0xFF,
                0x00,
                0x00,
                0x00,
                0xFF,
                0x00,
                0xFF,
                0x00,
                0x00,
                0xFF,
                0xFF,
                0xFF,
                0x00,
                0xFF,
                0x00,
                0xFF,
                0xFF,
                0xFF,
                0xFF,
                0x00,
            ),
        ),
    )


def draw_scene():
    global vertex_list
    # vykresleni ctyr usecek, data o useckach jsou ulozeny ve vertex listu
    vertex_list.draw(GL_LINES)


def clear_buffers():
    # vymazani vsech bitovych rovin barvoveho bufferu
    glClear(GL_COLOR_BUFFER_BIT)


def set_projection_matrix(nearPlane, farPlane):
    # zacatek modifikace projekcni matice
    glMatrixMode(GL_PROJECTION)
    # vymazani projekcni matice (=identita)
    glLoadIdentity()


def set_modelview_matrix():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # nahrat jednotkovou matici


@window.event
def on_draw():
    clear_buffers()
    set_projection_matrix(nearPlane, farPlane)
    set_modelview_matrix()
    draw_scene()  # vykresleni sceny


vertex_list = prepare_scene()
pyglet.app.run()
