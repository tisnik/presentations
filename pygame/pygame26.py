#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 26: použití objektů typu Surface, metoda blit()
#                   a operace pygame.transform.scale().


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
pygame.display.set_caption("Pygame test #26")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)

# Vyplnění plochy okna černou barvou
display.fill(BLACK)


# Načtení obrázku, který se bude vykreslovat a transformovat
image_surface = pygame.image.load(os.path.join("images", "pygame.png"))

# Rozměry původního obrázku
image_width = image_surface.get_width()
image_height = image_surface.get_height()

scale_ratio = 1.5

# Vytvoření zvětšených obrázků
horizontally_scaled_image = pygame.transform.scale(
    image_surface, (int(image_width * scale_ratio), image_height)
)

vertically_scaled_image = pygame.transform.scale(
    image_surface, (image_width, int(image_height * scale_ratio))
)

scaled_image = pygame.transform.scale(
    image_surface, (int(image_width * scale_ratio), int(image_height * scale_ratio))
)

# Přímé vykreslení původního obrázku
display.blit(image_surface, (50, 25))

# Přímé vykreslení zvětšených obrázků
display.blit(horizontally_scaled_image, (150, 25))
display.blit(vertically_scaled_image, (50, 125))
display.blit(scaled_image, (150, 125))


# Hlavní herní smyčka
while True:
    # Načtení a zpracování všech událostí z fronty
    for event in pygame.event.get():
        # Uzavřením okna běh aplikace ukončí
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Klávesou ESC se běh aplikace ukončí
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(20)

# finito
