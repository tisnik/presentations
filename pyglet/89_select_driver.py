#!/usr/bin/env python

import pyglet

pyglet.options["audio"] = ("pulse", "openal", "silent")

source = pyglet.media.load("login.wav", streaming=False)

source.play()
pyglet.app.run()
