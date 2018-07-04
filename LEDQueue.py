# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:37:07 2018

@author: Brendan
"""
from base import LEDBase as base
import queue as q

#%%
class LEDQueue(q.Queue):
  def __init__(self):
    self.queue = q.Queue.__init__(self)
    self.sources = {}
    
  def put(self, *kwargs):
    return self.queue.put(*kwargs)

  def get(self, *kwargs):
    return self.queue.get(*kwargs)
    
  def task_done(self, *kwargs):
    return self.queue.task_done(*kwargs)
#%%
class LEDInputSource(base):
  def __init__(self, name, queue):
    self.name = name
    self.queue = queue
    
  def event():
    pass
  
  def pass_message(self, command):
    msg = QueueMessage(self.name, command)
    self._add_queue(msg)
  
  def _add_queue(self, msg):
    self.queue.put(msg)
#%%
class QueueMessage(base):  
  def __init__(self, source, command):
    self.time = self._get_dttm()
    self.name = 'generic_message'
    self.source = source
    self.parse_command(command)
  
  def parse_command(self, cmd):
    if cmd.lower() in self.KNOWN_CMDS:
      code = self.KNOWN_CMDS.get(cmd)
      self.name = cmd
      return code
    else:
      self._raise_cmd_err(cmd)
  
  def _raise_cmd_err(self, cmd):
    self.name = 'ERRONEOUS COMMAND'
    raise ValueError('QueueMessage VALUE ERROR: %s IS AN UNKNOWN COMMAND'%cmd)
  
if __name__ == '__main__':
  lq = LEDQueue()