#!/usr/bin/python
# vim: set fileencodings=utf-8

import matplotlib

matplotlib.use("Agg")
import os
import sys

import numpy as np

import matplotlib.pyplot as plt
import pygame

# nutno importovat kvuli konstantam QUIT atd.
from pygame.locals import *

# velikost okna na obrazovce (framebufferu)
WIDTH = 640
HEIGHT = 480

# jmeno souboru s grafem
IMAGE_FILE = "plot2.png"

# jmeno zarizeni implementujiciho rozhrani k framebufferu
FRAMEBUFFER_DEVICE = "/dev/fb0"


# Vytvoreni grafu
def create_graph():
    fig = plt.figure()
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    return fig


# Ulozeni grafu do souboru
def save_graph(fig, imageFile):
    plt.savefig(
        imageFile,
        facecolor=fig.get_facecolor(),
        bbox_inches="tight",
        dpi=80,
        pad_inches=0.03,
    )


# Inicializace knihovny Pygame, inicializace video systemu a otevreni
# framebufferu
def initialize_pygame(width, height, background_color, framebuffer_device):
    os.environ["SDL_FBDEV"] = framebuffer_device
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.mouse.set_visible(0)
    screen.fill(background_color)
    return screen


# Zobrazeni rastroveho obrazku do framebufferu
def show_image(screen, imageFile):
    image = pygame.image.load(imageFile)
    screen.blit(image, (0, 0))
    pygame.display.flip()


# Cekani na ukonceni aplikace libovolnou klavesou
def wait_for_key():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                return
        clock.tick(20)


# Ukonceni aplikace
def exit():
    pygame.quit()
    sys.exit()


# Hlavni funkce aplikace
def main():
    fig = create_graph()
    save_graph(fig, IMAGE_FILE)
    screen = initialize_pygame(WIDTH, HEIGHT, (0, 0, 200), FRAMEBUFFER_DEVICE)
    show_image(screen, IMAGE_FILE)
    wait_for_key()
    exit()


# Vstupni bod
if __name__ == "__main__":
    main()
