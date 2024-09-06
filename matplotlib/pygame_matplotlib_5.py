#!/usr/bin/python
# vim: set fileencodings=utf-8

import matplotlib

matplotlib.use("Agg")
import os
import re
import subprocess
import sys

import numpy as np

import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pygame

# nutno importovat kvuli konstantam QUIT atd.
from pygame.locals import *

# DPI (umele zvolena hodnota)
DPI = 100

# jmeno souboru s grafem
IMAGE_FILE = "plot5.png"

# jmeno zarizeni implementujiciho rozhrani k framebufferu
FRAMEBUFFER_DEVICE = "/dev/fb0"


# Vytvoreni grafu
def create_graph(width, height, dpi):
    fig = plt.figure(figsize=(1.0 * width / dpi, 1.0 * height / dpi), dpi=dpi)
    delta = 0.1

    # prubeh nezavisle promenne x
    x = np.arange(-10.0, 10.0, delta)

    # prubeh nezavisle promenne y
    y = np.arange(-10.0, 10.0, delta)

    # vytvoreni dvou poli se souradnicemi [x,y]
    X, Y = np.meshgrid(x, y)

    # vzdalenost od bodu [0,0]
    R1 = np.sqrt(X * X + Y * Y)

    # vzdalenost od bodu [3,3]
    R2 = np.sqrt((X - 3) * (X - 3) + (Y - 3) * (Y - 3))

    # vypocet funkce, kterou pouzijeme pri vykreslovani grafu
    Z = np.sin(R1) - np.cos(R2)

    # povoleni zobrazeni mrizky
    plt.grid(True)

    # vytvoreni grafu s konturami funkce z=f(x,y)
    plt.contour(X, Y, Z)

    # zobrazeni grafu
    plt.plot()
    return fig


# Ulozeni grafu do souboru
def save_graph(fig, imageFile, dpi):
    plt.savefig(imageFile, facecolor=fig.get_facecolor(), dpi=dpi)


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
    image_rect = image.get_rect()
    screen_rect = screen.get_rect()
    x = (screen_rect.width - image_rect.width) / 2
    y = (screen_rect.height - image_rect.height) / 2
    screen.blit(image, (x, y))
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


# precteni aktualne nastaveneho rozliseni framebufferu
def get_framebuffer_resolution(framebuffer_device):
    fbset_output = subprocess.check_output(["fbset", "-s", "-fb", framebuffer_device])

    for line in fbset_output.split("\n"):
        line = line.strip()
        if line.startswith("geometry"):
            print(line)
            parsed = re.match(r"geometry (\d+) (\d+)", line)
            return (int(parsed.group(1)), int(parsed.group(2)))


# Ukonceni aplikace
def exit():
    pygame.quit()
    sys.exit()


# Hlavni funkce aplikace
def main():
    width, height = get_framebuffer_resolution(FRAMEBUFFER_DEVICE)
    fig = create_graph(width, height, DPI)
    save_graph(fig, IMAGE_FILE, DPI)
    screen = initialize_pygame(width, height, (10, 10, 40), FRAMEBUFFER_DEVICE)
    show_image(screen, IMAGE_FILE)
    wait_for_key()
    exit()


# Vstupni bod
if __name__ == "__main__":
    main()
