#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 27: použití objektů typu Surface, metoda blit()
#                   a operace pygame.transform.smoothscale().


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
pygame.display.set_caption("Pygame test #27")

# Konstanty s n-ticemi představujícími základní barvy
BLACK = (0, 0, 0)

# Vyplnění plochy okna černou barvou
display.fill(BLACK)


# Načtení obrázku, který se bude vykreslovat a transformovat
image_surface = pygame.image.load(os.path.join("images", "pygame.png"))

# Rozměry původního obrázku
image_width = image_surface.get_width()
image_height = image_surface.get_height()

scale_ratio = 3

# Vytvoření zvětšených obrázků
horizontally_scaled_image = pygame.transform.scale(
    image_surface, (int(image_width * scale_ratio), image_height)
)

horizontally_smooth_scaled_image = pygame.transform.smoothscale(
    image_surface, (int(image_width * scale_ratio), image_height)
)

vertically_scaled_image = pygame.transform.scale(
    image_surface, (image_width, int(image_height * scale_ratio))
)

vertically_smooth_scaled_image = pygame.transform.smoothscale(
    image_surface, (image_width, int(image_height * scale_ratio))
)

smooth_scaled_image = pygame.transform.smoothscale(
    image_surface, (int(image_width * scale_ratio), int(image_height * scale_ratio))
)

# Přímé vykreslení původního obrázku
display.blit(image_surface, (10, 10))

# Přímé vykreslení zvětšených obrázků
display.blit(horizontally_scaled_image, (170, 10))
display.blit(horizontally_smooth_scaled_image, (170, 90))
display.blit(vertically_scaled_image, (10, 170))
display.blit(vertically_smooth_scaled_image, (90, 170))
display.blit(smooth_scaled_image, (170, 170))

# Načtení fontu (zadává se soubor se jménem fontu a velikost
font = pygame.font.Font("fonts/FreeSans.ttf", 40)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Vytvoření obrázku s vykresleným textem
# - první parametr obsahuje řetězec, který se má vykreslit
# - druhý parametr řídí použití antialiasingu
# - třetí parametr volí barvu fontu
font_surface1 = font.render(
    pygame.transform.get_smoothscale_backend(), True, WHITE, RED
)

# Vykreslení obrázku s nápisem do bufferu
display.blit(font_surface1, (15, 100))


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
