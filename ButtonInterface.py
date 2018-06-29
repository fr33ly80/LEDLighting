# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:28:01 2018

@author: Brendan
"""
from LEDQueue import LEDInputSource

class ButtonInterface(LEDInputSource):
    
    def TurnOn(self):
        pass
    
    def TurnOff(self):
        pass
      
      
      
#%% Class Examples
class Animal():
  def __init__(self, name):
    self.name = name
    self.size = 10.
    
  def eat(self):
    print(self.name+' ate!')
    
  def sleep(self):
    pass


class Lion(Animal):
  def __init__(self, name):
    self.name = name
  
  def kill(self):
    pass
  
  def eat(self):
    pass
    
    
a = Animal('Lion')


a.kill()
