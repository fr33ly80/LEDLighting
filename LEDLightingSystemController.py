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
      self.queue = Queue()
      self.lamp = Lamp()
      self.log = Log()
      self.ON = True
      self.set_default_state()
      
    def set_default_state(self):
      self.execute(self.default_mode)
      
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
      pass
    
    def lamp_off(self, msg=None):
      pass
    
    def rainbow(self, msg=None):
      pass
    
    def wipe(self, msg=None):
      pass
    
    def clear(self, msg=None):
      pass
    
    def theater(self, msg=None):
      pass
    
    def cycle(self, msg=None):
      pass
    
    def set_color(self, msg='000'):
      pass