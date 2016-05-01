#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import K_DOWN
from pygame.locals import K_UP
from pygame.locals import K_RIGHT
from pygame.locals import K_LEFT
from pygame.locals import K_SPACE
from pygame.locals import KEYDOWN
from pygame.locals import K_ESCAPE
from Menu import GameMenu
from Tools import Position
from Tools import Utilities
from Tools import Character
from Tools import Hero

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
    main_menu = True
    #INIT FOR TESTS
    position = Position(100,150)
    background = Utilities.load_image("HFMegaPak\Backgrounds\Badland 1.png", IMG_DIR, alpha=False)
    scene_background = Utilities.load_image("HFMegaPak\Backgrounds\Badlands 2.png", IMG_DIR, alpha=False)
    gm = GameMenu(screen,background)
    screen.blit(gm.background,(0,0))
    #Utilities.load_sound(gm.song,SONIDO_DIR)
    character_image = Utilities.load_image("HFMegaPak\HF1_Remaster\Characters\Male_Elf_14\Male_Elf_14_HF1R_Face.png", IMG_DIR, alpha=False)
    player = Hero("Alejandro",character_image,Position(300,400),1000,100,1000,100)
    pygame.key.set_repeat(1, 80)
    #END INIT FOR TESTS
    while mainloop:
        # Limit frame speed to 50 FPS
        clock.tick(50)
        if main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        player.position.moveDown()
                        for item in gm.items:
                            if item[0] == "Start":
                                item[1] = gm.font.render(item[0], 1, (255,255,255))
                                item[4] = False
                            elif item[0] == "Quit":
                                item[1] = gm.font.render(item[0], 1, (0,0,0))
                                item[4] = True
                    elif event.key == K_UP:
                        player.position.moveUp()
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
                    elif event.key == K_ESCAPE:
                        mainloop = False

            for name, label, (width, height), (posx, posy), selected in gm.items:
                screen.blit(label, (posx, posy))
                pygame.display.flip()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        player.position.move_down()
                    elif event.key == K_UP:
                        player.position.move_up()
                    if event.key == K_RIGHT:
                        player.position.move_right()
                    elif event.key == K_LEFT:
                        player.position.move_left()                        
                    elif event.key == K_ESCAPE:
                        mainloop = False

            font_player = pygame.font.SysFont(None, 12)
            screen.blit(scene_background,(0,0))
            screen.blit(font_player.render(str(player),1,(255,255,255)), player.get_position())
            pygame.display.flip()