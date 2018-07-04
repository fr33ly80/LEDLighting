# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:29:48 2018

@author: Brendan
"""
from base import LEDBase as base
from LEDController import NeopixelLEDController as Lamp
from LEDQueue import LEDQueue as Queue
from LEDLog import Log
import time

class LEDLightingSystemController(base):
    def __init__(self):
      self.default_mode = '002'
      
    def start(self):
      self.Queue = Queue()
      self.Lamp = Lamp()
      self.Log = Log()
      self.ON = True
      
    def run(self):
      msg = self._check_queue()
      if msg:
        self.log(msg)
        cmd = self.parse_msg()
        self.execute(cmd, msg)
      time.sleep(.5)
      if self.ON:
        self.run()
        
    def parse_msg(self, msg):
      if msg[0:3] in self.KNOWN_CMDS.keys():
        cmd = self.KNOWN_CMDS.get(msg[0:3])
        return cmd
      else:
        self._log_error(msg)
        
    def _log_error(self, msg):
      self.Log.log(self.name, msg)

    def log(self, msg):
      code = msg[0:3]
      self.Log.log(self.name, code, msg)
    
    def execute(self, cmd, msg):
      cmd(msg)
      
    def lamp_on(self, msg=None):
      self.Lamp.begin()
      self.default_mode()
    
    def lamp_off(self, msg=None):
      pass
    
    def rainbow(self, msg=None):
      pass
    
    def wipe(self, msg='000100200240'):
      red = int(msg[3:6])
      green = int(msg[6:9])
      blue = int(msg[9:12])
      color = self.Lamp.Color(red, blue, green)
      self.Lamp.colorWipe(color)
    
    def clear(self, msg=None):
      color = self.Lamp.Color(0, 0, 0)
      self.Lamp.colorWipe(color)
    
    def theater(self, msg=None):
      pass
    
    def cycle(self, msg=None):
      pass
    
    def set_color(self, msg='000100200240'):
      red = int(msg[3:6])
      green = int(msg[6:9])
      blue = int(msg[9:12])
      color = self.Lamp.Color(red, blue, green)
      self.Lamp.solidColor(color)
      pass