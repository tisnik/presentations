#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 28: použití objektů typu Surface, metoda blit()
#                   a operace pygame.transform.rotate()
#                   + pygame.transform.rotozoom().


import pygame
import sys
import os

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# Velikost okna aplikace
WIDTH = 400
HEIGHT = 400

# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #28")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)

# Vyplnění plochy okna černou barvou
display.fill(BLACK)


# Načtení obrázku, který se bude vykreslovat a transformovat
image_surface = pygame.image.load(os.path.join("images", "pygame.png"))

# Vytvoření otočených obrázků
rot90_image = pygame.transform.rotate(image_surface, 90)
rot180_image = pygame.transform.rotate(image_surface, 180)
rot270_image = pygame.transform.rotate(image_surface, 270)
rot45_image = pygame.transform.rotate(image_surface, 45)
rotm45_image = pygame.transform.rotate(image_surface, -45)
rot_and_scaled_image_1 = pygame.transform.rotozoom(image_surface, 30, 0.7)
rot_and_scaled_image_2 = pygame.transform.rotozoom(image_surface, 30, 2.0)

# Přímé vykreslení původního obrázku
display.blit(image_surface, (20, 25))

# Přímé vykreslení otočených obrázků
display.blit(rot90_image, (115, 25))
display.blit(rot180_image, (210, 25))
display.blit(rot270_image, (305, 25))
display.blit(rot45_image, (20, 125))
display.blit(rotm45_image, (20, 245))
display.blit(rot_and_scaled_image_1, (220, 120))
display.blit(rot_and_scaled_image_2, (200, 200))


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
