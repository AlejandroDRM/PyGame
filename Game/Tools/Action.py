#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Action(object):

    def __init__(self,function):
        self.function = function

    def run(self):
        self.function()    