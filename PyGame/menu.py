#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import pygame
import utilities
from pygame.locals import *
 
# -----------
# Constantes
# -----------
 
WIDTH = 900
HEIGHT = 600
IMG_DIR = "resources\imgs"
SONIDO_DIR = "resources\sounds"
# WIDTH = 640
# HEIGHT = 480
 
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------

class GameMenu():
    
    def __init__(self, screen, items, bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.screen = screen
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.items = []
        for item in items:
            label = self.font.render(item, 1, font_color)
            self.items.append(label)
 
    def run(self):
        mainloop = True
        utilities.load_sound("Medieval\prologue.mp3",SONIDO_DIR)
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
 
            # Redraw the background
            self.screen.fill(self.bg_color)
            for label in self.items:
                self.screen.blit(label, (100, 100))
            pygame.display.flip()
            
# ------------------------------
# Funci�n principal del juego
# ------------------------------
if __name__ == "__main__":
    pygame.init()
    menu_items = ('Start', 'Quit')
    # Creating the screen
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen,menu_items)
    gm.run()