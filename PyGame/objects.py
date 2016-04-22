#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class Button():
    def __init__(self,label,state,color,x_axis,y_axis,action):
        self.label = label
        self.state = state
        self.color = color
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.action = action

class Door():

    def __init__(self,state,x_axis,y_axis,action):
        self.state = state
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.action = action

class Action():

    def __init__(self,function):
        self.function = function

    def run(self):
        self.function()	

class Character(pygame.sprite.Sprite):
    
    def __init__(self,image,position,max_health,max_mana):
        self.position = position
        self.max_health = max_health
        self.max_mana = max_mana
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

class Hero(Character):
    
    def __init__(self,image,position,max_health,max_mana,current_health,current_mana):
        pygame.sprite.Sprite.__init__(self)
        Character.__init__(self,image,position,max_health,max_mana)
        self.current_health = current_health
        self.current_mana = current_mana

class Position():	

    def __init__(self,x_axis,y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def MoveUp(self):
        self.y_axis += 5

    def MoveDown(self):
        self.y_axis -= 5

    def MoveRight(self):
        self.x_axis += 5

    def MoveLeft(self):
        self.x_axis -= 5
        
        