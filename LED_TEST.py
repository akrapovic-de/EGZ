import time
from time import sleep
import board
import neopixel

# The number of NeoPixels
num_pixels = 200
# Pin the LED_Strip is connected
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

pixel_pin = board.D18
# pixel_pin = GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

pixels[0] = (255, 0, 0)  # rot