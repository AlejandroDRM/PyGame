#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import pygame
from pygame.locals import *
import sys
import os
 
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
def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print "Error, no se puede cargar la imagen: ", ruta
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

def load_sound(nombre, dir_sonido):
    ruta = os.path.join(dir_sonido, nombre)
    # Intentar cargar el sonido
    try:
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()
    except pygame.error, message:
        sonido = None
 
# ------------------------------
# Funci�n principal del juego
# ------------------------------
 
def main():
    pygame.init()
    pygame.mixer.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    # se define la letra por defecto
    fuente = pygame.font.Font(None, 20)
     # se crea un proyectil a lanzar
    pygame.key.set_repeat(1, 80) # Activa repetici�n de teclas
    clock = pygame.time.Clock()
    # el bucle principal del juego
    load_sound("Medieval\prologue.mp3", SONIDO_DIR)
    while True:
        clock.tick(60)
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
        pygame.display.flip()
 
 
if __name__ == "__main__":
    main()