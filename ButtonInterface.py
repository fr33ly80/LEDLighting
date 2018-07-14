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
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BCM) # Use bcm pin numbering
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be input channel and set initial value to be low current (off)
        self.channel = 10
        
    # Collection of button actions & pass strings
    #Do these need "channel" as an input?
    def turn_button_on(self):
        passString = "997"
        return passString
    
    def turn_button_off(self):
        passString = "998"
        return passString
    
    def clear_led(self):
        passString = "999"
        return passString
    
    def led_solid_color(self, rgb):
        passString = "000" + str(rgb)
        return passString
    
    def led_rainbow(self):
        passString = "001"
        return passString
    
    def led_wipe(self):
        passString = "002"
        return passString
    
    def led_theater_chase(self):
        passString = "003"
        return passString
    
    def query_last_setting(self):
        #Don't know how to do this yet
        passString = "XXX"
        return passString
    
    def start(self,channel):

    # We start at low current and go to high so we want to detect RISING
    # Turn button on by passing string "997" 
        GPIO.add_event_detect(10,GPIO.RISING,callback=turn_button_on)
    
        #Once LED is on, wait for up to 20 seconds for a rising edge (timeout is in ms)
        event = GPIO.wait_for_edge(self.channel, GPIO_RISING, timeout=20000)
        
        if event is None:
            #Turn button off is temporary
            turn_button_off()
            #query_last_setting()
        
        if event is True:
    
            #https://raspberrypi.stackexchange.com/questions/63512/how-can-i-detect-how-long-a-button-is-pressed
            start_time = time.time()
            
            while GPIO.input(channel) == True: #Wait for the button to be low (i.e. high value is true).
                pass
            
            buttonTime = time.time() - start_time #How long was the button down?
            
                
            if buttonTime >= .1:
                event = GPIO.add_event_detect(channel, GPIO_RISING)
                if GPIO.event_detected(channel):
                    rgb == "123123234" #red
                    led_solid_color(channel, rgb)
                    time.sleep(0.1)
                    
                if GPIO.event_detected(channel):
                    rgb == "235" #yellow
                    led_solid_color(channel, rgb)
                
            elif buttonTime > 2.:
                event = GPIO.add_event_detect(channel, GPIO_RISING)
                if GPIO.event_detected(channel):
                    led_rainbow()
                    time.sleep(0.1)
                
                event = GPIO.add_event_detect(channel, GPIO_RISING)
                if GPIO.event_detected(channel):
                    led_wipe()
                    time.sleep(0.1)
                
                event = GPIO.add_event_detect(channel, GPIO_RISING)
                if GPIO.event_detected(channel):
                    led_theater_chase()
        
            else:
                print("Don't think I need an else here?")
        
        
        GPIO.cleanup() # Clean up    
        
    
"""
What I want the button to do:
    Press once to turn on 
    If don't press again within 20 seconds, turn leds off
        Ideally want to be return to last setting
    If long hold:
        Cycle through colors by short-pressing button
        Press button once for red, twice for yellow, etc
    If no long hold (short press):
        Press button once for rainbow 001
        Press button twice for wipe 002
        Press button three times for theater chase lights 003

    
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
