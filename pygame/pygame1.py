#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 1: kostra aplikace, v níž se používá
#                  knihovna Pygame


import sys

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import QUIT

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240

# Inicializace knihovny Pygame
pygame.init()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #1")


# Hlavní herní smyčka
while True:
    # Načtení a zpracování všech událostí z fronty
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# finito
