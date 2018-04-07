# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:30:28 2018

@author: Brendan
"""

from LampInterface import LampInterface

class LEDLampImplementation(LampInterface):
    def __init__(self):
        self.knownCommands = {'idle':self.idle,
                              'colorwheel':self.color_wheel,
                              'rainbow':self.rainbow,
                              'blink':self.blink,
                              'breathe':self.breathe,
                              'flash':self.flash,
                              'pathway':self.pathway}
    
    def command(self, command):
        pass
    
    def execute(self, command):
        pass
    
    def idle(self):
        pass
    
    def color_wheel(self):
        pass
    
    def rainbow(self):
        pass
    
    def blink(self):
        pass
    
    def breathe(self):
        pass
    
    def flash(self):
        pass
    
    def pathway(self):
        pass    