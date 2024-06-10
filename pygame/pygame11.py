#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 11: některé další vlastnosti objektů typu Surface.


import pygame
import sys
import os
import math

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import QUIT, K_ESCAPE, KEYDOWN

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240

# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #11")

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

# Vykreslení čar různou barvou
pygame.draw.line(display, BLUE, (10, 10), (160, 10))
pygame.draw.line(display, CYAN, (10, 20), (160, 20))
pygame.draw.line(display, GREEN, (10, 30), (160, 30))
pygame.draw.line(display, YELLOW, (10, 40), (160, 40))
pygame.draw.line(display, RED, (10, 50), (160, 50))
pygame.draw.line(display, MAGENTA, (10, 60), (160, 60))

# Vykreslení čar s různým sklonem
for i in range(1, 90, 5):
    # převod ze stupňů na radiány
    angle = math.radians(i)
    radius = 150
    # výpočet koncových bodů úseček
    x = radius * math.sin(math.radians(i))
    y = radius * math.cos(math.radians(i))

    if display.get_bitsize() >= 24:
        # vykreslení jedné antialiasované úsečky, blend je nastaveno na True
        pygame.draw.aaline(display, WHITE, (WIDTH - 1, 0), (WIDTH - x, y), True)
    else:
        # vykreslení jedné úsečky
        pygame.draw.line(display, WHITE, (WIDTH - 1, 0), (WIDTH - x, y))

# Vykreslení čar různou šířkou
for i in range(1, 10):
    pygame.draw.line(display, WHITE, (10 + i * 15, 90), (10 + i * 15, 230), i)


image_surface = pygame.image.load(os.path.join("images", "gnome-globe.png"))

# Výpočet souřadnic pro umístění obrázku přesně doprostřed okna
center_x = (display.get_width() - image_surface.get_width()) / 2
center_y = (display.get_height() - image_surface.get_height()) / 2

# Vykreslení obrázku
display.blit(image_surface, (center_x, center_y))


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
