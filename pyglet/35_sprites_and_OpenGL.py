#!/usr/bin/env python

import pyglet
from pyglet.gl import *

window = pyglet.window.Window(width=450, height=350, caption="Pyglet+OpenGL")

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load("gnome-globe.png", file=image_stream)

sprite = pyglet.sprite.Sprite(image)
sprite.dx = 1
sprite.dy = 1


def draw_points():
    glColor3f(1.0, 1.0, 1.0)  # nastaveni barvy pro kresleni
    glBegin(GL_POINTS)  # nyni zacneme vykreslovat body
    glVertex2i(50, 50)
    glVertex2i(100, 50)
    glVertex2i(100, 100)
    glVertex2i(50, 100)
    glEnd()


def draw_lines():
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_LINES)  # nyni zacneme vykreslovat usecky
    glVertex2i(150, 50)
    glVertex2i(200, 50)
    glVertex2i(200, 100)
    glVertex2i(150, 100)
    glEnd()


def draw_line_strip():
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)  # nyni vykreslime polycaru
    glVertex2i(250, 50)
    glVertex2i(300, 50)
    glVertex2i(300, 100)
    glVertex2i(250, 100)
    glEnd()


def draw_line_loop():
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)  # nyni vykreslime uzavrenou polycaru
    glVertex2i(350, 50)
    glVertex2i(400, 50)
    glVertex2i(400, 100)
    glVertex2i(350, 100)
    glEnd()


def draw_triangles():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)  # vykresleni trojuhelniku
    glVertex2i(50, 150)
    glVertex2i(100, 150)
    glVertex2i(100, 200)
    glVertex2i(50, 200)
    glEnd()


def draw_triangle_strip():
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_STRIP)  # vykresleni pruhu trojuhelniku
    glVertex2i(150, 150)
    glVertex2i(150, 200)
    glVertex2i(200, 200)
    glVertex2i(200, 150)
    glEnd()


def draw_triangle_fan():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)  # vykresleni trsu trojuhelniku
    glVertex2i(300, 150)
    glVertex2i(250, 160)
    glVertex2i(270, 190)
    glVertex2i(290, 200)
    glVertex2i(310, 200)
    glVertex2i(330, 190)
    glVertex2i(350, 160)
    glEnd()


def draw_quads():
    glColor3f(1.0, 0.5, 0.5)
    glBegin(GL_QUADS)  # vykresleni ctyruhelniku
    glVertex2i(50, 250)
    glVertex2i(100, 250)
    glVertex2i(100, 300)
    glVertex2i(50, 300)
    glEnd()


def draw_quad_strip():
    glColor3f(0.5, 0.5, 1.0)
    glBegin(GL_QUAD_STRIP)  # vykresleni pruhu ctyruhleniku
    glVertex2i(150, 250)
    glVertex2i(150, 300)
    glVertex2i(200, 240)
    glVertex2i(200, 310)
    glVertex2i(250, 260)
    glVertex2i(250, 290)
    glVertex2i(300, 250)
    glVertex2i(300, 300)
    glEnd()


def draw_polygon():
    glColor3f(0.5, 1.0, 0.5)
    glBegin(GL_POLYGON)  # vykresleni konvexniho polygonu
    glVertex2i(350, 260)
    glVertex2i(370, 240)
    glVertex2i(390, 240)
    glVertex2i(410, 260)
    glVertex2i(410, 280)
    glVertex2i(390, 300)
    glVertex2i(370, 300)
    glVertex2i(350, 280)
    glEnd()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_points()

    draw_lines()
    draw_line_strip()
    draw_line_loop()

    draw_triangles()
    draw_triangle_strip()
    draw_triangle_fan()

    draw_quads()
    draw_quad_strip()

    draw_polygon()

    sprite.draw()


def update(dt):
    sprite.x += sprite.dx * dt * 200
    sprite.y += sprite.dy * dt * 200
    if sprite.x < 0:
        sprite.x = 0
        sprite.dx = -sprite.dx
    if sprite.y < 0:
        sprite.y = 0
        sprite.dy = -sprite.dy
    if sprite.x + sprite.width > window.width:
        sprite.x = window.width - sprite.width
        sprite.dx = -sprite.dx
    if sprite.y + sprite.height > window.height:
        sprite.y = window.height - sprite.height
        sprite.dy = -sprite.dy


pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
