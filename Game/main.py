#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import K_DOWN
from pygame.locals import K_UP
from pygame.locals import K_SPACE
from pygame.locals import KEYDOWN
from pygame.locals import K_ESCAPE
from Menu import GameMenu
from Tools import Position
from Tools import Utilities

# -----------
# Constants
# -----------

WIDTH = 640
HEIGHT = 480
IMG_DIR = "resources\imgs"
SONIDO_DIR = "resources\sounds"

# ------------------------------
# Main Loop
# ------------------------------
if __name__ == "__main__":
    pygame.init()
    # Creating the screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
    pygame.display.set_caption('Game Menu')
    mainloop = True
    position = Position(100,150)
    background = Utilities.load_image("HFMegaPak\Backgrounds\Badland 1.png", IMG_DIR, alpha=False)
    gm = GameMenu(screen,background)
    Utilities.load_sound(gm.song,SONIDO_DIR)
    screen.blit(gm.background,(0,0))
    main_menu = True
    while mainloop:
        # Limit frame speed to 50 FPS
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    for item in gm.items:
                        if item[0] == "Start":
                            item[1] = gm.font.render(item[0], 1, (255,255,255))
                            item[4] = False
                        elif item[0] == "Quit":
                            item[1] = gm.font.render(item[0], 1, (0,0,0))
                            item[4] = True
                elif event.key == K_UP:
                    for item in gm.items:
                        if item[0] == "Start":
                            item[1] = gm.font.render(item[0], 1, (0,0,0))
                            item[4] = True
                        elif item[0] == "Quit":
                            item[1] = gm.font.render(item[0], 1, (255,255,255))
                            item[4] = False
                elif event.key == K_ESCAPE:
                    mainloop = False
        if main_menu:
            # Redraw the background
            for name, label, (width, height), (posx, posy), selected in gm.items:
                screen.blit(label, (posx, posy))
                pygame.display.flip()

