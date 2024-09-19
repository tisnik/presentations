#!/usr/bin/env python

import pyglet

GRAY = (128, 128, 128, 255)
RED = (255, 128, 128, 255)


def create_window(width, height):
    return pyglet.window.Window(width=width, height=height, caption="Pyglet library")


def create_gray_label(text, x, y, anchor_x, anchor_y):
    return pyglet.text.Label(
        text, font_size=18, x=x, y=y, anchor_x=anchor_x, anchor_y=anchor_y, color=GRAY
    )


window = create_window(640, 480)
label = create_gray_label("Mouse:", 10, 10, "left", "bottom")


@window.event
def on_draw():
    window.clear()
    label.draw()


button_names = {
    pyglet.window.mouse.LEFT: "left",
    pyglet.window.mouse.RIGHT: "right",
    pyglet.window.mouse.MIDDLE: "middle",
}


def on_mouse_action(x, y, button, action):
    button_name = button_names.get(button, "unknown")
    text = format("Mouse %s %s button at [%d, %d]" % (action, button_name, x, y))
    label.text = text
    print(text)
    on_draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    on_mouse_action(x, y, button, "pressed")


@window.event
def on_mouse_release(x, y, button, modifiers):
    on_mouse_action(x, y, button, "released")


pyglet.app.run()
