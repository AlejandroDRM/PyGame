#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utilities
import objects
import pygame
import menu
from pygame.locals import *
# -----------
# Constantes
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
    gm = menu.GameMenu(screen)
    mainloop = True
    utilities.load_sound(gm.song,SONIDO_DIR)
    screen.blit(gm.background,(0,0))
    main_menu = True
    character_image = utilities.load_image("HFMegaPak\HF1_Remaster\Characters\Male_Elf_14\Male_Elf_14_HF1R_Face.png", IMG_DIR, alpha=False)
    player = objects.Hero(character_image,(300,400),1000,100,1000,100)
    while mainloop:
        # Limit frame speed to 50 FPS
        clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
                
            if event.type == pygame.KEYDOWN and main_menu:
                if event.key == K_DOWN:
                    for item in gm.items:
                        if item[0] == "Start":
                            item[1] = gm.font.render(item[0], 1, (255,255,255))
                            item[4] = False
                        elif item[0] == "Quit":
                            item[1] = gm.font.render(item[0], 1, (0,0,0))
                            item[4] = True                            
                elif event.key == K_UP and main_menu:
                    for item in gm.items:
                        if item[0] == "Start":
                            item[1] = gm.font.render(item[0], 1, (0,0,0))
                            item[4] = True
                        elif item[0] == "Quit":
                            item[1] = gm.font.render(item[0], 1, (255,255,255))
                            item[4] = False
                elif event.key == K_SPACE and main_menu:
                    for item in gm.items:
                        if item[0] == "Start" and item[4] == True:
                            main_menu = False
                        elif item[0] == "Quit" and item[4] == True:
                            mainloop = False
                                             
            if main_menu:                            
                # Redraw the background
                for name, label, (width, height), (posx, posy), selected in gm.items:
                    screen.blit(label, (posx, posy))
                    pygame.display.flip()
                
            else:
                scene_background = utilities.load_image("HFMegaPak\Backgrounds\Badlands 2.png", IMG_DIR, alpha=False)
                screen.blit(scene_background,(0,0))
                todos = pygame.sprite.RenderPlain(player)
                todos.draw(screen)
                pygame.display.flip()
