#!/usr/bin/env python

import pyglet

source = pyglet.media.load("login.wav", streaming=False)

source.play()
pyglet.app.run()
