#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 24: použití spritů, pohyblivý sprite,
#                   kolize, různé tvary kolidujících spritů
#                   kolize se korektně počítá pro kruhové sprity


import sys

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import K_ESCAPE, KEYDOWN, KEYUP, QUIT

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240


# Třída představující sprite zobrazený jako jednobarevný čtverec.
class CircularSprite(pygame.sprite.Sprite):
    # Konstruktor
    def __init__(self, x, y, radius, normal_image_name, collision_image_name):
        # Nejprve je nutné zavolat konstruktor předka,
        # tj. konstruktor třídy pygame.sprite.Sprite:
        pygame.sprite.Sprite.__init__(self)

        # Načtení obrázků, jeden pro normální sprite,
        # druhý pro sprite, který koliduje s hráčem
        self.normal_image = pygame.image.load("images/" + normal_image_name + ".png")

        self.collision_image = pygame.image.load(
            "images/" + collision_image_name + ".png"
        )

        # Vytvoření obrázku představujícího vizuální obraz spritu:
        self.image = self.normal_image
        # self.image.fill(color) - toto nyní nepoužijeme,
        #                          pozůstatek z BlockySprite

        # Vytvoření obalového obdélníku
        # (velikost se získá z rozměru obrázku)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # U kulatých spritů se nastavuje i poloměr
        self.radius = radius

        # Počáteční rychlost spritu
        self.speed_x = 0
        self.speed_y = 0

    # Nastavení obrázku u spritu, který kolidoval s hráčem
    def setCollisionImage(self):
        self.image = self.collision_image

    # Nastavení obrázku u spritu, který nekolidoval s hráčem
    def setNormalImage(self):
        self.image = self.normal_image


# Inicializace knihovny Pygame
pygame.init()

clock = pygame.time.Clock()

# Vytvoření okna pro vykreslování
display = pygame.display.set_mode([WIDTH, HEIGHT])

# Nastavení titulku okna
pygame.display.set_caption("Pygame test #24")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)

# Objekt sdružující všechny sprity
all_sprites = pygame.sprite.Group()
# Objekt sdružující všechny sprity kromě hráče
all_sprites_but_player = pygame.sprite.Group()

# Vytvoření několika typů spritů
#                       x    y   r  první obr. druhý obr.
wall1 = CircularSprite(20, 40, 31, "sprite3", "sprite2")
wall2 = CircularSprite(20, 140, 31, "sprite3", "sprite2")
wall3 = CircularSprite(220, 40, 31, "sprite3", "sprite2")
wall4 = CircularSprite(220, 140, 31, "sprite3", "sprite2")
wall5 = CircularSprite(120, 40, 31, "sprite3", "sprite2")
wall6 = CircularSprite(120, 140, 31, "sprite3", "sprite2")
player = CircularSprite(WIDTH / 2 - 20, HEIGHT / 2 - 20, 22, "sprite1", "sprite1")

# Přidání několika dalších spritů do seznamu
# (jen jeden sprite - ten poslední - bude ve skutečnosti pohyblivý)
all_sprites.add(wall1)
all_sprites.add(wall2)
all_sprites.add(wall3)
all_sprites.add(wall4)
all_sprites.add(wall5)
all_sprites.add(wall6)
all_sprites.add(player)

# Seznam všech nepohyblivých spritů
all_sprites_but_player.add(wall1)
all_sprites_but_player.add(wall2)
all_sprites_but_player.add(wall3)
all_sprites_but_player.add(wall4)
all_sprites_but_player.add(wall5)
all_sprites_but_player.add(wall6)


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


# Změna obrázku spritu na základě kolize s hráčem
def change_sprite_image(sprite_group, hit_list):
    # Projít všemi sprity ze skupiny, kterou detekovala kolizní funkce
    for sprite in sprite_group:
        if sprite in hit_list:
            sprite.setCollisionImage()
        else:
            sprite.setNormalImage()


# Zjistí kolize spritu se "stěnami" (nepohyblivými sprity)
def check_collisions(player, sprite_group):
    # Vytvoření seznamu spritů, které kolidují s hráčem
    hit_list = pygame.sprite.spritecollide(
        player, sprite_group, False, pygame.sprite.collide_circle
    )
    # Změna obrázků kolidujících spritů
    change_sprite_image(sprite_group, hit_list)
    collisions = len(hit_list)
    # Přenastavení titulku okna
    caption = "Pygame test #24: collisions " + str(collisions)
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
