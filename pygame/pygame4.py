#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 4: vykreslení základních geometrických
#                  tvarů s využitím modulu pygame.draw.


import pygame
import sys

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
pygame.display.set_caption("Pygame test #4")

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

# Vykreslení čar různou šířkou
for i in range(1, 10):
    pygame.draw.line(display, WHITE, (10 + i * 15, 80), (10 + i * 15, 210), i)

# Základní geometrické tvary: kruh, vyplněný čtverec, elipsa a čtverec
pygame.draw.circle(display, CYAN, (280, 40), 20, 0)
pygame.draw.rect(display, RED, (280 - 20, 80, 40, 40))
pygame.draw.ellipse(display, YELLOW, (280 - 30, 140, 60, 40))
pygame.draw.rect(display, MAGENTA, (280 - 20, 190, 40, 40), 1)


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
