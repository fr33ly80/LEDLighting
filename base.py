# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:59:39 2018

@author: Brendan
"""

import datetime

class LEDBase():
  DTTM_FMT = '%m/%d/%Y %H:%M:%S'
  DEBUG = True
  
  def __init__(self):
    self.birthdate = self.get_dttm()
    self.KNOWN_CMDS = {'998': self.lamp_off, 
                       '997': self.lamp_on, 
                       '001': self.rainbow,
                       '002': self.wipe,
                       '003': self.theater,
                       '999': self.clear,
                       '000': self.set_color}
    self.KNOWN_CODES = {'ON'     :'997',
                        'OFF'    :'998',
                        'RAINBOW':'001',
                        'WIPE'   :'002',
                        'THEATER':'003',
                        'CLEAR'  :'999',
                        'COLOR'  :'000'} 
    self.KNOWN_COLORS = {'red'   :'XXXXXX'}
    
  def get_dttm(self):
    dttm = datetime.datetime.now()
    dttm = dttm.strftime(self.DTTM_FMT)
    return dttm

  def _remove_keys(self, dictionary, rm_keys):    
    keep = []
    temp = {}
    for key in dictionary.keys():
        if key not in rm_keys:
            keep.append(key)       
    for key in keep:
        temp[key] = dictionary.get(key)
    return temp