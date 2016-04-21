#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utilities
import pygame
import menu
from pygame.locals import *
# -----------
# Constantes
# -----------
 
WIDTH = 900
HEIGHT = 600
IMG_DIR = "resources\imgs"
SONIDO_DIR = "resources\sounds"

# ------------------------------
# Main Loop
# ------------------------------
if __name__ == "__main__":
    pygame.init()
    # Creating the screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('Game Menu')
    gm = menu.GameMenu(screen)
    mainloop = True
    utilities.load_sound(gm.song,SONIDO_DIR)
    screen.blit(gm.background,(0,0))
    while mainloop:
        # Limit frame speed to 50 FPS
        clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False

        # Redraw the background
        for name, label, (width, height), (posx, posy) in gm.items:
            screen.blit(label, (posx, posy))
        pygame.display.flip()