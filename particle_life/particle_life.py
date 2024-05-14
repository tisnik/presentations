# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import sys
from enum import Enum
from math import sqrt
from random import random

import pygame
import pygame.locals

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Particle life simulator"

# Constants used by model
RED_GROUP = 0
GREEN_GROUP = 1
YELLOW_GROUP = 2
BLUE_GROUP = 3

# Model options
BORDER = 50

# Number of particles of different colors/attributes
MAX_RED = 1000
MAX_GREEN = 200
MAX_BLUE = 50
MAX_YELLOW = 10

# Total number of particles in the whole system
MAX_PARTICLES = MAX_RED+MAX_GREEN+MAX_BLUE+MAX_YELLOW

# Other model options
MAX_DISTANCE = 2000
DAMPING_FACTOR = 0.5
SLOW_DOWN_FACTOR = 0.1
SCALE_FACTOR = 1


class Colors(Enum):
    """Named colors used everywhere on demo screens."""

    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)


class Particle:
    def __init__(self, x : float, y : float, vx : float, vy : float, type : int):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.type = type


class Atoms:
    def __init__(self, max_particles : int):
        self.colors = (0xffff0000, 0xff00ff00, 0xff2020ff, 0xffffff00)
        self.particles = []
        self.particles += (create_particles(MAX_RED, RED_GROUP))
        self.particles += (create_particles(MAX_GREEN, GREEN_GROUP))
        self.particles += (create_particles(MAX_BLUE, BLUE_GROUP))
        self.particles += (create_particles(MAX_YELLOW, YELLOW_GROUP))
        print("Particles in atoms:", len(self.particles))


class Model:
    def __init__(self, max_particles : int):
        self.rules = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        self.init_rules()
        self.atoms = Atoms(max_particles)

    def init_rules(self):
        for j in range(4):
            for i in range(4):
                self.rules[i][j] = 2.0*random() - 1.0


def random_x() -> float:
    return (WINDOW_WIDTH - BORDER*2) * random() + BORDER


def random_y() -> float:
    return (WINDOW_HEIGHT - BORDER*2) * random() + BORDER


def create_particles(max : int, type : int):
    return [Particle(random_x(), random_y(), 0.0, 0.0, type) for i in range(max)]


def redraw(surface, model):
    surface.fill(Colors.BLACK.value)
    atoms = model.atoms
    for particle in atoms.particles:
        color = atoms.colors[particle.type]
        surface.set_at((int(particle.x),int(particle.y)), color)
        surface.set_at((int(particle.x-1),int(particle.y)), color)
        surface.set_at((int(particle.x+1),int(particle.y)), color)
        surface.set_at((int(particle.x),int(particle.y-1)), color)
        surface.set_at((int(particle.x),int(particle.y+1)), color)


def apply_rules(model : Model):
    for i in range(len(model.atoms.particles)):
        fx : float = 0.0
        fy : float = 0.0

        a = model.atoms.particles[i]

        # compute force for selected particle
        for j in range(len(model.atoms.particles)):
            if i != j:
                b = model.atoms.particles[j]
                g = model.rules[a.type][b.type] * SCALE_FACTOR
                dx = a.x - b.x
                dy = a.y - b.y
                if dx != 0.0 or dy != 0.0:
                    d = dx*dx + dy*dy
                    if d < MAX_DISTANCE:
                        f = g / sqrt(d)
                        fx += f * dx
                        fy += f * dy

        # apply force to selected particle
        a.vx = (a.vx + fx) * DAMPING_FACTOR
        a.vy = (a.vy + fy) * DAMPING_FACTOR

        # move particle
        a.x += a.vx
        a.y += a.vy

        # check if particle touches scene boundary
        if a.x <= 0:
            a.vx = -a.vx
            a.x = 0

        if a.x >= WINDOW_WIDTH:
            a.vx = -a.vx
            a.x = WINDOW_WIDTH - 1

        if a.y <= 0:
            a.vy = -a.vy
            a.y = 0

        if a.y >= WINDOW_HEIGHT:
            a.vy = -a.vy
            a.y = WINDOW_HEIGHT - 1


def write_particles(model, filename):
    atoms = model.atoms
    with open(filename, "w") as fout:
        fout.write('"x","y"\n')
        for particle in atoms.particles:
            fout.write(f"{particle.x},{particle.y}\n")


# set window title
pygame.display.set_caption(WINDOW_TITLE)

display = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
display.fill(Colors.BLACK.value)

surface = pygame.Surface([WINDOW_WIDTH, WINDOW_HEIGHT])
surface.set_at((101,100), 0xffff0000)
surface.set_at((100,101), 0xffff0000)
surface.set_at((101,101), 0xffff0000)

clock = pygame.time.Clock()
model = Model(MAX_PARTICLES)

"""Event loop for About screen that just waits for keypress or window close operation."""
while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.locals.K_RETURN:
                pygame.quit()
                sys.exit()
            if event.key == pygame.locals.K_w:
                write_particles(model, "particles.csv")

    # all events has been processed - update scene and redraw the screen
    apply_rules(model)
    redraw(surface, model)
    display.blit(surface, (0, 0))
    pygame.display.update()
    # clock.tick(25)
