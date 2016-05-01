#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Position(object):    

    def __init__(self,x_axis,y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis
        
    def moveUp(self):
        self.y_axis += 5

    def moveDown(self):
        self.y_axis -= 5

    def moveRight(self):
        self.x_axis += 5

    def moveLeft(self):
        self.x_axis -= 5
        
    def __str__(self):
        return "X_Axis: %d Y_Axis: %d" % (self.x_axis, self.y_axis)