#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Character(object):
    
    def __init__(self,image,position,max_health,max_mana):
        self.position = position
        self.max_health = max_health
        self.max_mana = max_mana
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position.x_axis
        self.rect.centery = self.position.y_axis