#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Character import *

class Hero(Character):

    def __init__(self,name,image,position,max_health,max_mana,current_health,current_mana):
        Character.__init__(self,name,image,position,max_health,max_mana)
        self.current_health = current_health
        self.current_mana = current_mana

    def __str__(self):
        return ("%s %s" % (self.name,str(self.position)))

