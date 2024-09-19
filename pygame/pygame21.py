#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 21: použití spritů, pohyblivý sprite


import sys

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import K_ESCAPE, KEYDOWN, KEYUP, QUIT

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

        # Počáteční rychlost spritu
        self.speed_x = 0
        self.speed_y = 0


# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #21")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Objekt sdružující všechny sprity
all_sprites = pygame.sprite.Group()
# Objekt sdružující všechny sprity kromě hráče
all_sprites_but_player = pygame.sprite.Group()

# Vytvoření několika typů spritů
#                     barva  x   y velikost
wall1 = BlockySprite(GRAY, 50, 10, 10)
wall2 = BlockySprite(GRAY, 15, 100, 100)
wall3 = BlockySprite(GRAY, 15, 100, 150)
wall4 = BlockySprite(GRAY, 15, 200, 100)
wall5 = BlockySprite(GRAY, 15, 200, 150)
player = BlockySprite(RED, 25, WIDTH / 2 - 12, HEIGHT / 2 - 12)

# Přidání několika dalších spritů do seznamu
# (jen jeden sprite - ten poslední - bude ve skutečnosti pohyblivý)
all_sprites.add(wall1)
all_sprites.add(wall2)
all_sprites.add(wall3)
all_sprites.add(wall4)
all_sprites.add(wall5)
all_sprites.add(player)

# Seznam všech nepohyblivých spritů
all_sprites_but_player.add(wall1)
all_sprites_but_player.add(wall2)
all_sprites_but_player.add(wall3)
all_sprites_but_player.add(wall4)
all_sprites_but_player.add(wall5)


# Posun všech spritů ve skupině na základě jejich rychlosti
def move_sprites(sprite_group, playground_width, playground_height):
    for sprite in sprite_group:
        # Posun spritu
        sprite.rect.x = sprite.rect.x + sprite.speed_x
        sprite.rect.y = sprite.rect.y + sprite.speed_y
        # Kontrola, zda sprite nenarazil do okrajů okna
        if sprite.rect.x < 0:
            sprite.rect.x = 0
            sprite.speed_x = 0
        if sprite.rect.x + sprite.rect.width > playground_width:
            sprite.rect.x = playground_width - sprite.rect.width
            sprite.speed_x = 0
        if sprite.rect.y < 0:
            sprite.rect.y = 0
            sprite.speed_y = 0
        if sprite.rect.y + sprite.rect.height > playground_height:
            sprite.rect.y = playground_height - sprite.rect.height
            sprite.speed_y = 0


# Vykreslení celé scény na obrazovku
def draw_scene(display, background_color, sprite_group):
    # Vyplnění plochy okna černou barvou
    display.fill(background_color)
    # Vykreslení celé skupiny spritů do bufferu
    sprite_group.draw(display)
    # Obnovení obsahu obrazovky (překlopení zadního a předního bufferu)
    pygame.display.update()


# Zjistí kolize spritu se "stěnami" (nepohyblivými sprity)
def check_collisions(player, sprite_group):
    # Vytvoření seznamu spritů, které kolidují s hráčem
    hit_list = pygame.sprite.spritecollide(player, sprite_group, False)
    collisions = len(hit_list)
    # Přenastavení titulku okna
    caption = "Pygame test #21: collisions " + str(collisions)
    pygame.display.set_caption(caption)


# Hlavní herní smyčka
while True:
    # Načtení a zpracování všech událostí z fronty
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Stiskem kurzorových kláves je možné měnit směr pohybu spritu
            elif event.key == pygame.K_LEFT:
                player.speed_x = -3
            elif event.key == pygame.K_RIGHT:
                player.speed_x = +3
            elif event.key == pygame.K_UP:
                player.speed_y = -3
            elif event.key == pygame.K_DOWN:
                player.speed_y = +3
        if event.type == KEYUP:
            # Puštění kurzorových kláves vede k zastavení pohybu spritu
            if event.key == pygame.K_LEFT:
                player.speed_x = 0
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 0
            elif event.key == pygame.K_UP:
                player.speed_y = 0
            elif event.key == pygame.K_DOWN:
                player.speed_y = 0

    move_sprites(all_sprites, display.get_width(), display.get_height())
    check_collisions(player, all_sprites_but_player)
    draw_scene(display, BLACK, all_sprites)
    clock.tick(20)

# finito
