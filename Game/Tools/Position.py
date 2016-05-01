#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Position(object):

    def __init__(self,x_axis,y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def move_up(self):
        self.y_axis -= 5

    def move_down(self):
        self.y_axis += 5

    def move_right(self):
        self.x_axis += 5

    def move_left(self):
        self.x_axis -= 5

    def __str__(self):
        return "(%d,%d)" % (self.x_axis, self.y_axis)

    def get_position(self):
        return (self.x_axis, self.y_axis)

