# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:35:28 2018

@author: Brendan
"""

_TEST_MODE = True

import time
if _TEST_MODE:
    from neopixel import _Mock_Adafruit_NeoPixel as npxl
else:
    from neopixel import Adafruit_Neopixel as npxl
from neopixel import Color

class NeopixelLEDController(npxl):
    # LED strip configuration as of 4/10/2018:
    LED_COUNT      = 144      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
    #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    def __init__(self):
        npxl.__init__(self)
    
    # Define functions which animate LEDs in various ways.
    def colorWipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)
            self.show()
            time.sleep(wait_ms/1000.0)
    
    def theaterChase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i+q, color)
                self.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i+q, 0)
    
    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)
    
    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(self.numPixels()):
                self.setPixelColor(i, self.wheel((i+j) & 255))
            self.show()
            time.sleep(wait_ms/1000.0)
    
    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.numPixels()):
                color = self.wheel((int(i*256/self.numPixels()) + j)%255)
                self.setPixelColor(i, color)
            self.show()
            time.sleep(wait_ms/1000.0)
    
    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i+q, self.wheel((i+j) % 255))
                self.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i+q, 0)