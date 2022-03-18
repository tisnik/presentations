#!/usr/bin/env python

import pyglet

image_stream = open("gnome-globe.png", "rb")
image = pyglet.image.load("gnome-globe.png", file=image_stream)

print("Loaded image with size %d x %d pixels" % (image.width, image.height))
