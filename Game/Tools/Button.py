#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Button(object):
    def __init__(self,label,state,color,x_axis,y_axis,action):
        self.label = label
        self.state = state
        self.color = color
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.action = action