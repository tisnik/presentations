#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 17: použití spritů


import pygame, sys, os, math

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import QUIT, K_ESCAPE, KEYDOWN

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240


# Třída představující sprite zobrazený jako jednobarevný čtverec.
class BlockySprite(pygame.sprite.Sprite):
    # Konstruktor
    def __init__(self, color, size, x, y):
        # Nejprve je nutné zavolat konstruktor předka,
        # tj. konstruktor třídy pygame.sprite.Sprite:
        pygame.sprite.Sprite.__init__(self)

        # Vytvoření obrázku představujícího vizuální obraz spritu:
        self.image = pygame.Surface([size, size])
        self.image.fill(color)

        # Vytvoření obalového obdélníku
        # (velikost se získá z rozměru obrázku)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #17")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Vyplnění plochy okna černou barvou
display.fill(BLACK)

# Objekt sdružující všechny sprity
all_sprites = pygame.sprite.Group()

# Vytvoření dvojice spritů
sprite1 = BlockySprite(RED, 50, 10, 10)
sprite2 = BlockySprite(BLUE, 25, 50, 10)

# Přidání dvojice spritů do seznamu
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Vykreslení celé skupiny spritů do bufferu
all_sprites.draw(display)


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
