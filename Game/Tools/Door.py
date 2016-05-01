#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Door(object):

    def __init__(self,state,x_axis,y_axis,action):
        self.state = state
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.action = action