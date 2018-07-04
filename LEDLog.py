# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:58:35 2018

@author: Brendan
"""

import pandas
import os

from base import LEDBase as base

class Log(base):
  LOG_PATH = r'\logs\LEDlog.csv'
  ARC_PATH = r'\logs\archive\\'
  HEADERS = ['timestamp', 'code', 'type', 'description']
  
  def __init__(self):
    self.cwd = os.getcwd()
    self.LOG_PATH = self.cwd+self.LOG_PATH
    self._open_log()
    self._wakeup()
  
  def _open_log(self):
    try:
      self.log = pandas.read_csv(self.LOG_PATH)
    except:
      if self.DEBUG: print('\n\nNo existing log found')
      self._new_log()
      self._open_log()
  
  def _new_row(self, row):
    row = pandas.DataFrame([row], columns=self.HEADERS)
    return row
  
  def _new_log(self):
    if self.DEBUG: print('\n\nNew log being written to %s'%self.LOG_PATH)
    log = self._new_row([])
    self._save(log)
  
  def _wakeup(self):
    string = [self.get_dttm(), 'WAKE', 'wakeup', 'Log System Init']
    self._write(string)
    self._save(self.log)
  
  def _write(self, string):
    if self.DEBUG: print('\n\nWriting to log: ', string)
    row = self._new_row(string)
    self.log = self.log.append(row)
    self._save(self.log)
    
  def log(self, source, code, string):
    string = [self.get_dttm(), code, source, string]
    self._write(string)
    
  def log_error(self, source, string):
    string = [self.get_dttm(), 'ERROR', source, string]
    self._write(string)
  
  def _save(self, log):
    #save log
    if self.DEBUG: print('\n\nSaving LED Log')
    log.to_csv(self.LOG_PATH, index=False)
  
  def _clear_log(self):
    row = self._new_row([])
    self.log = row
  
  def _archive(self):
    self.log.to_csv(self.ARC_PATH, index=False)