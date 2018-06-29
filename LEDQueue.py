# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:37:07 2018

@author: Brendan
"""
import queue

class LEDQueue(queue.Queue):
  def __init__(self):
    self.queue = queue.Queue.__init__(self)
    self.sources = {}
    
  def put(self, *kwargs):
    return self.queue.put(*kwargs)

  def get(self, *kwargs):
    return self.queue.get(*kwargs)
    
  def task_done(self, *kwargs):
    return self.queue.task_done(*kwargs)

class LEDInputSource():
  def __init__(self, name):
    self.name = name
    self.queue = queue
    
  def event():
    pass
  
  def add_queue():
    pass
  
if __name__ == '__main__':
  lq = LEDQueue()