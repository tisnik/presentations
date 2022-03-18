#!/usr/bin/env python

import pyglet


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def load_cursor(filename):
    image = pyglet.image.load(filename)
    return pyglet.window.ImageMouseCursor(image, image.width / 2, image.height / 2)


window = create_window(640, 480)
custom_cursor = load_cursor("gnome-globe.png")


@window.event
def on_draw():
    window.clear()


cursors = {
    pyglet.window.key.F1: pyglet.window.Window.CURSOR_DEFAULT,
    pyglet.window.key.F2: pyglet.window.Window.CURSOR_HAND,
    pyglet.window.key.F3: pyglet.window.Window.CURSOR_HELP,
    pyglet.window.key.F4: pyglet.window.Window.CURSOR_SIZE,
    pyglet.window.key.F5: pyglet.window.Window.CURSOR_SIZE_UP,
    pyglet.window.key.F6: pyglet.window.Window.CURSOR_SIZE_DOWN,
    pyglet.window.key.F7: pyglet.window.Window.CURSOR_SIZE_LEFT,
    pyglet.window.key.F8: pyglet.window.Window.CURSOR_SIZE_RIGHT,
    pyglet.window.key.F9: pyglet.window.Window.CURSOR_WAIT,
    pyglet.window.key.F10: pyglet.window.Window.CURSOR_NO,
}


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        cursor = custom_cursor
    else:
        cursor_type = cursors.get(symbol)
        cursor = window.get_system_mouse_cursor(cursor_type)
    window.set_mouse_cursor(cursor)


pyglet.app.run()
