#!/usr/bin/env python

import pyglet
from pyglet.gl import *
from pyglet.window import key

fov = 70.0  # hodnota zorneho uhlu - field of view
nearPlane = 0.1  # blizsi orezavaci rovina
farPlane = 90.0  # vzdalenejsi orezavaci rovina

r1 = 0.0
r2 = 0.0

depthBufferEnabled = False  # povoleni ci zakaz Z-bufferu

window = pyglet.window.Window(width=500, height=500, caption="Pyglet+OpenGL")


keys = key.KeyStateHandler()
window.push_handlers(keys)


def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)  # barva pozadi obrazku
    glClearDepth(1.0)  # implicitni hloubka ulozena v pameti hloubky
    glPolygonMode(GL_FRONT, GL_FILL)  # nastaveni rezimu vykresleni vyplnenych sten
    glPolygonMode(GL_BACK, GL_FILL)  # jak pro predni tak pro zadni steny
    glDisable(GL_CULL_FACE)  # zadne hrany ani steny se nebudou odstranovat
    glDepthFunc(GL_LESS)  # funkce pro testovani fragmentu
    glEnable(GL_BLEND)  # povoleni blendingu
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)  # viditelna oblast pres cele okno


def draw_walls():
    glBegin(GL_QUADS)  # vykresleni otevrene krychle - sten domecku
    glColor4f(0.0, 0.0, 1.0, 0.5)  # modra barva steny
    glVertex3f(-5.0, -5.0, -5.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glVertex3f(5.0, -5.0, 5.0)
    glVertex3f(5.0, -5.0, -5.0)

    glColor4f(0.0, 1.0, 0.0, 0.5)  # zelena barva steny
    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, -5.0)

    glColor4f(1.0, 0.0, 0.0, 0.5)  # cervena barva steny
    glVertex3f(-5.0, -5.0, -5.0)
    glVertex3f(-5.0, -5.0, 5.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, -5.0)

    glColor4f(1.0, 1.0, 0.0, 0.5)  # zluta barva steny
    glVertex3f(5.0, -5.0, -5.0)
    glVertex3f(5.0, -5.0, 5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, -5.0)
    glEnd()


def draw_roof():
    glBegin(GL_TRIANGLES)  # vykresleni strechy domecku z trojuhelniku
    glColor4f(0.0, 1.0, 1.0, 0.5)
    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(5.0, 5.0, -5.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor4f(1.0, 0.0, 1.0, 0.5)
    glVertex3f(5.0, 5.0, -5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor4f(1.0, 1.0, 1.0, 0.5)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(0.0, 11.0, 0.0)

    glColor4f(0.0, 0.0, 0.0, 0.5)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(0.0, 11.0, 0.0)
    glEnd()


def set_depth_buffer(depthBufferEnabled):
    if depthBufferEnabled:
        glEnable(GL_DEPTH_TEST)
    else:
        glDisable(GL_DEPTH_TEST)


def clear_buffers(depthBufferEnabled):
    if depthBufferEnabled:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # vymazani i Z/W bufferu
    else:
        glClear(GL_COLOR_BUFFER_BIT)  # vymazani vsech bitovych rovin barvoveho bufferu


@window.event
def on_draw():
    global r1, r2
    global depthBufferEnabled

    if keys[key.LEFT]:
        r2 = r2 - 1
    if keys[key.RIGHT]:
        r2 = r2 + 1
    if keys[key.UP]:
        r1 = r1 - 1
    if keys[key.DOWN]:
        r1 = r1 + 1
    if keys[key.E]:
        depthBufferEnabled = True
    if keys[key.D]:
        depthBufferEnabled = False

    clear_buffers(depthBufferEnabled)
    set_depth_buffer(depthBufferEnabled)

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

    draw_walls()
    draw_roof()


pyglet.app.run()
