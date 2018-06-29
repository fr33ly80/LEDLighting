# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:29:48 2018

@author: Brendan
"""
from LEDController import NeopixelLEDController as Lamp
from LEDQueue import LEDQueue as Queue
import time

class LEDLightingSystemController():
    def __init__(self):
      self.default_mode = '002'
      self.KNOWN_CMDS = {'000': self.lamp_off, 
                         '001': self.lamp_on, 
                         '002': self.rainbow,
                         '003': self.wipe,
                         '999': self.clear}
      
    def start(self):
      self.queue = Queue()
      self.lamp = Lamp()
      self.ON = True
      self.set_default_state()
      
    def set_default_state(self):
      self.execute(self.default_mode)
      
    def run(self):
      msg = self._check_queue()
      if msg:
        self.log(msg)
        cmd = self.parse_msg()
        self.execute(cmd)
      time.sleep(.5)
      if self.ON:
        self.run()
        
    def parse_msg(self, msg):
      if msg in self.KNOWN_CMDS.keys():
        cmd = self.KNOWN_CMDS.get(msg)
        return cmd
      else:
        self._log_error(msg)
        
    def _log_error(self, msg):
      pass

    def log(self, msg):
      pass
    
    def execute(self, cmd):
      cmd()