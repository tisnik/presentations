#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 3: další ze způsobů snížení zatížení
#                  procesoru v hlavní smyčce událostí


import sys

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import QUIT

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240

# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #3")


# Hlavní herní smyčka
while True:
    # Načtení a zpracování všech událostí z fronty
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(20)

# finito
