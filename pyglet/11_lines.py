#!/usr/bin/env python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající knihovnu Pyglet

import pyglet
from pyglet.gl import *

# vytvoření okna
window = pyglet.window.Window(width=450,
                              height=350,
                              caption="Pyglet+OpenGL")


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    patterns=[0xff00, 0xf0f0, 0xcccc, 0x5555, 0xfe10, 0x5e32]

    glDisable(GL_LINE_SMOOTH)                   # zakazani antialiasingu usecek
    glDisable(GL_LINE_STIPPLE)                  # zakazani maskovani pixelu na care

    glLineWidth(1.0)                            # tloustka usecky je jeden pixel
    glBegin(GL_LINES) 
    for i in xrange(0, 10):                     # vykresleni prvni rady usecek ruzne barvy
        step = i/10.0
        glColor3f(step, 0.0, 1.0-step)          # zmena barvy uvnitr prikazovych "zavorek" glBegin()/glEnd()
        glVertex2f(50.0+300.0*step, 20.0) 
        glColor3f(step, 1.0, 1.0-step) 
        glVertex2f(100.0+300.0*step, 70.0) 
    glEnd() 

    for i in xrange(0, 10):                     # vykresleni druhe rady usecek ruzne tloustky
        step = i/10.0
        glLineWidth(step*10.0+0.1)              # zmena tloustky usecky
        glBegin(GL_LINES) 
        glColor3f(step, 0.0, 1.0-step)          # zmena barvy uvnitr prikazovych "zavorek" glBegin()/glEnd()
        glVertex2f(50.0+300.0*step, 90.0) 
        glColor3f(step, 1.0, 1.0-step) 
        glVertex2f(100.0+300.0*step, 140.0) 
        glEnd() 

    glEnable(GL_LINE_SMOOTH)                    # povoleni antialiasingu usecek
    for i in xrange(0, 10):                     # vykresleni treti rady usecek ruzne tloustky
        step= i/10.0
        glLineWidth(step*10.0+0.1)              # zmena tloustky usecky
        glBegin(GL_LINES) 
        glColor3f(step, 0.0, 1.0-step)          # zmena barvy uvnitr prikazovych "zavorek" glBegin()/glEnd()
        glVertex2f(50.0+300.0*step, 160.0) 
        glColor3f(step, 1.0, 1.0-step) 
        glVertex2f(100.0+300.0*step, 210.0) 
        glEnd() 

    glDisable(GL_LINE_SMOOTH)                   # zakazani antialiasingu usecek
    glEnable(GL_LINE_STIPPLE)                   # povoleni maskovani pixelu na care
    glLineWidth(1.0)                            # tloustka usecky je jeden pixel
    glColor3f(1.0, 1.0, 1.0)                    # zmena barvy vne prikazovych "zavorek" glBegin()/glEnd()

    for i in xrange(0, 6):
        glLineStipple(2, patterns[i])           # nastaveni masky pri kresleni usecek
        glBegin(GL_LINES) 
        glVertex2i(50, 250+i*20)                # vykresleni usecky
        glVertex2i(350, 250+i*20) 
        glEnd() 


pyglet.app.run()

