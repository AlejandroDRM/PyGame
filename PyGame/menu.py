#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import utilities
from pygame.locals import *
 

IMG_DIR = "resources\imgs"
SONIDO_DIR = "resources\sounds"
 
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------

class GameMenu():
    
    def __init__(self, screen,  bg_color=(0,0,0), font=None, font_size=30,
                    font_color=(255, 255, 255)):
        self.menu_items = ('Start', 'Quit')
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.items = []
        self.background = utilities.load_image("HFMegaPak\Backgrounds\Badland 1.png", IMG_DIR, alpha=False)
        self.song = "Medieval\prologue.mp3"
        for index, item in enumerate(self.menu_items):
            if(item == "Start"):
                label = self.font.render(item, 1, (0,0,0))
                selected = True
            elif item == "Quit":
                label = self.font.render(item, 1, font_color)
                selected = False
            width = label.get_rect().width
            height = label.get_rect().height
            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(self.menu_items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
            self.items.append([item, label, (width, height), (posx, posy),selected])
