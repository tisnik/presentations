#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 5: přístup k pixelům vybraného objektu
#                  typu Surface.


import sys

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import QUIT

# Velikost okna aplikace
WIDTH = 256
HEIGHT = 256

# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #5")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)

# Vyplnění plochy okna černou barvou
display.fill(BLACK)

# Získání dvourozměrného pole s hodnotami pixelů
pixelArray = pygame.PixelArray(display)

# Změna barev některých pixelů
for y in xrange(HEIGHT):
    for x in xrange(WIDTH):
        pixelArray[x][y] = (x, y, (x + y) % 256)

# Pixely byly změněny, pole je možné odstranit z paměti
# a současně tak uvolnit surface pro další operace
del pixelArray


# Hlavní herní smyčka
while True:
    # Načtení a zpracování všech událostí z fronty
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(20)

# finito
