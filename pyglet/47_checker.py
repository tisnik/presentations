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
texturesEnabled = True  # povoleni ci zakaz textur

minFilterEnabled = True  # filtry pouzite pri texturovani
magFilterEnabled = True


def create_window():
    return pyglet.window.Window(width=500, height=500, caption="Pyglet library")


window = create_window()


def load_texture(filename):
    image_stream = open(filename, "rb")
    image = pyglet.image.load(filename, file=image_stream)
    return image.get_texture()


def init():
    glClearColor(0.0, 0.0, 0.3, 0.0)  # barva pozadi obrazku
    glPolygonMode(GL_FRONT, GL_FILL)  # nastaveni rezimu vykresleni modelu
    glPolygonMode(GL_BACK, GL_FILL)
    glDisable(GL_CULL_FACE)  # zadne hrany ani steny se nebudou odstranovat
    glDepthFunc(GL_LESS)  # funkce pro testovani fragmentu

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, texture.id)

    glEnable(GL_TEXTURE_2D)  # povoleni texturovani


@window.event
def on_resize(width, height):
    init()
    glViewport(0, 0, width, height)  # viditelna oblast pres cele okno


def draw_floor():
    glBegin(GL_QUADS)  # vykresleni podlahy
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-50.0, -5.0, -50.0)
    glTexCoord2f(5.0, 0.0)
    glVertex3f(-50.0, -5.0, 50.0)
    glTexCoord2f(5.0, 5.0)
    glVertex3f(50.0, -5.0, 50.0)
    glTexCoord2f(0.0, 5.0)
    glVertex3f(50.0, -5.0, -50.0)
    glEnd()


def set_depth_buffer(depthBufferEnabled):
    if depthBufferEnabled:
        glEnable(GL_DEPTH_TEST)
    else:
        glDisable(GL_DEPTH_TEST)


def clear_buffers(depthBufferEnabled):
    if depthBufferEnabled:  # vymazani i Z/W bufferu
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    else:  # vymazani vsech bitovych rovin barvoveho bufferu
        glClear(GL_COLOR_BUFFER_BIT)


def set_filters(minFilterEnabled, magFilterEnabled):
    minFilter = GL_LINEAR if minFilterEnabled else GL_NEAREST
    magFilter = GL_LINEAR if magFilterEnabled else GL_NEAREST
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, minFilter)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, magFilter)


def set_textures(texturesEnabled):
    if texturesEnabled:
        glEnable(GL_TEXTURE_2D)
    else:
        glDisable(GL_TEXTURE_2D)


@window.event
def on_draw():
    global depthBufferEnabled
    global texturesEnabled
    global minFilterEnabled
    global magFilterEnabled

    if keys[key.Z]:
        depthBufferEnabled = not depthBufferEnabled
    if keys[key.T]:
        texturesEnabled = not texturesEnabled
    if keys[key.I]:
        minFilterEnabled = not minFilterEnabled
    if keys[key.A]:
        magFilterEnabled = not magFilterEnabled

    clear_buffers(depthBufferEnabled)
    set_depth_buffer(depthBufferEnabled)
    set_filters(minFilterEnabled, magFilterEnabled)
    set_textures(texturesEnabled)

    # zacatek kodu modifikujiciho projekcni matici
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # vymazani projekcni matice
    gluPerspective(fov, 1.0, nearPlane, farPlane)

    # zacatek kodu modifikujiciho modelview matici
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
    glTranslatef(0, 0, -40)  # posun objektu

    draw_floor()  # vykresleni objektu - podlahy


texture = load_texture("checker.png")
keys = key.KeyStateHandler()
window.push_handlers(keys)

pyglet.app.run()
