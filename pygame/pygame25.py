#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 25: použití objektů typu Surface, metoda blit()
#                   a operace pygame.transform.flip().


import pygame
import sys
import os

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
pygame.display.set_caption("Pygame test #25")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)

# Vyplnění plochy okna černou barvou
display.fill(BLACK)


# Načtení obrázku, který se bude vykreslovat a transformovat
image_surface = pygame.image.load(os.path.join("images", "pygame.png"))

# Vytvoření zrcadlených obrázků
horizontally_flipped = pygame.transform.flip(image_surface, True, False)
vertically_flipped = pygame.transform.flip(image_surface, False, True)
both_flipped = pygame.transform.flip(image_surface, True, True)

# Přímé vykreslení původního obrázku
display.blit(image_surface, (50, 25))

# Přímé vykreslení zrcadlených obrázků
display.blit(horizontally_flipped, (150, 25))
display.blit(vertically_flipped, (50, 125))
display.blit(both_flipped, (150, 125))


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
