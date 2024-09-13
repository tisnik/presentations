#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 10: použití objektů typu Surface a metoda blit().


import os
import sys

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240

# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #10")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)

# Vyplnění plochy okna černou barvou
display.fill(BLACK)


image_surface = pygame.image.load(os.path.join("images", "gnome-globe.png"))

display.blit(image_surface, (0, 0))
display.blit(image_surface, (100, 100))


# Hlavní herní smyčka
while True:
    # Načtení a zpracování všech událostí z fronty
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(20)

# finito
