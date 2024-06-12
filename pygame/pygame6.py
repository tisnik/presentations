#!/usr/bin/python

# Demonstrační příklady využívající knihovnu Pygame

import pygame
import sys

# Příklad číslo 6: výpis seznamu všech dostupných grafických
#                  režimů pro zadané bitové hloubky.


# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import *

# Inicializace knihovny Pygame
pygame.init()

print("Driver: " + pygame.display.get_driver())
print("")

# Budou nás zajímat grafické režimy s bitovou hloubkou
# 8bpp (256 barev), 16bpp (hi-color), 24bpp a 32bpp (True Color)
for depth in [8, 16, 24, 32]:
    print("Graphics modes for %d bpp:" % depth)

    # Získat seznam grafických režimů pro danou bitovou hloubku
    gfx_modes = pygame.display.list_modes(depth)

    # Vypsat všechny získané režimy
    for gfx_mode in gfx_modes:
        print("    %d x %d pixels" % (gfx_mode[0], gfx_mode[1]))

pygame.quit()

# finito
