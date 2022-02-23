# Simple test for NeoPixels on Raspberry Pi
import RPi.GPIO as GPIO
import time
from time import sleep
import neopixel

# The number of NeoPixels
num_pixels = 144
# Pin the LED_Strip is connected
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pixel_pin = GPIO.setup(18, GPIO.OUT,initial=GPIO.LOW)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

status_door= input("ROS::status door?")

if status_door == "open":
	pixels[0:num_pixels] = (255, 0, 0) #rot
else:
	pixels[0:num_pixels] = (0,255,0) #green
