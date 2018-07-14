# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:28:01 2018

@author: Brendan
"""
from LEDQueue import LEDInputSource
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
    
# ButtonInterface inherits class LEDInputSource
class ButtonInterface(LEDInputSource):    
    def __init__(self):
        LEDInputSource.__init__(self)
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BCM) # Use bcm pin numbering
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be input channel and set initial value to be low current (off)
        self.channel = 10
        self._init_cycles()
        
        colors = []
        for key in self.KNOWN_COLORS.keys():
            colors.append(key)

        fn = []
        for key in self.KNOWN_CODES.keys():
            fn.append(key)
            #colors = (red, orange, yellow)
            
        self.on = "false"    
        self.mode = "color"
        self.current_color = "WHITE"
        self.current_mode = "THEATER"
        
    def _init_cycles(self):
        self.color_cycle = self.KNOWN_COLORS
        self.fn_cycle = self._remove_keys(self.KNOWN_COLORS,
                                          ['ON', 'OFF', 'CLEAR'])
    
    def button_pressed(self)
        length = self.detectLongOrShort()
        self.determine_cmd(length)
        
    def wait_for_button(self)    :
        GPIO.add_event_detect(10,GPIO.RISING,callback=button_pressed)
                            
    
    def detectLongOrShort(self)
        start_time = time.time()
        while GPIO.input(channel) == True: #Wait for the button to be low (i.e. high value is true).
            pass
        buttonTime = time.time() - start_time #How long was the button down?
        if buttonTime <= 1:
            length = "short"
            return length
        if 1 <= buttonTime <= 5 
            length = "long"
            return length
        if buttonTime >= 10:
            length = "superlong"
            return length
        
        GPIO.cleanup() # Clean up    
        
    def determine_cmd(self, length)
        if self.on:
            if length = "short"
                self.short_commmand()
            elif length = "long"
                if self.mode = "color"
                    self.mode = "fn"
                if self.mode = "fn"
                    self.mode = "color"
            else length = "superlong"
                offval = self.KNOWN_CODES.get("OFF)
                self.pass_message("OFF)
        return self.mode
    
    def short_command(self, mode):
        if mode = "color"
            self.cycle_color()
        else mode = "fn"
            self.cycle_fn()

    def cycle_color(self, dictionary, current_color):
        index = color.index(current_color)
        num_colors = length(colors)
        if index < num_colors:
            next_index = index + 1
        else:
            next_index = 0
        next_color = colors(next_index)
        next_color_value = dictionary.get(next_color)
        self.pass_message(next_color_value)
        current_color = next_color
        return current_color
    
    def cycle_fn(self, dictionary, current_fn):
        index = fn.index(current_fn)
        num_fm = length(fn)
        if index < num_fn:
            next_index = index + 1
        else:
            next_index = 0
        next_fn = fn(next_index)
        next_fn_value = dictionary.get(next_fn)
        self.pass_message(next_fn_value)
        return next_fn_value
        current_fn = next_fn
        return current_fn

 
"""

Goal of this code:
Pass message back to Queue with state of button
        Inherit method from LEDInputSource called "pass_message"
        String is going to be 3 digit number (string)
        
        System modes:
        999 = clear LED strip
        998 =  turn off
        997 = turn on
        
        Color modes:
        000rgb = one solid color
        001 = rainbow
        002 = wipe a single color
        003 = theater chase lights
    

"""

      
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
