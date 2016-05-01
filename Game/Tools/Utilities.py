#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

class Utilities(object):
    
    def __init__(self):
        self.message = "Utilities"
        
    @staticmethod 
    def load_image(nombre, dir_imagen, alpha=False):
        # Find route
        ruta = os.path.join(dir_imagen, nombre)
        try:
            image = pygame.image.load(ruta)
        except:
            print "Error, no se puede cargar la imagen: ", ruta
            sys.exit(1)
        # Check if the image has alpha channel
        if alpha == True:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image
    
    @staticmethod
    def load_sound(nombre, dir_sonido):
        ruta = os.path.join(dir_sonido, nombre)
        # Try to load sound
        try:
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play()
        except pygame.error, message:
            sonido = None