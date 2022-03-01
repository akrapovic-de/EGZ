import time
from time import sleep
import board
import neopixel

# The number of NeoPixels
num_pixels = 200
# Pin the LED_Strip is connected
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pixel_pin = board.D18
# pixel_pin = GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)


def blink_green():
    while True:
        for i in range(0, num_pixels):
            pixels[i] = (255, 0, 0)  # rot
        sleep(1)
        for i in range(0, num_pixels):
            pixels[i] = (0, 0, 0)  # rot
        sleep(1)
        status_door = input("ROS::status door (1-Abbruch)?")
        if status_door == "1":
            break


def cont_green():
    while True:
        for i in range(0, num_pixels):
            pixels[i] = (255, 0, 0)  # rot
        status_door = input("ROS::status door (1-Abbruch)?")
        if status_door == "1":
            break


def blink_red():
    while True:
        for i in range(0, num_pixels):
            pixels[i] = (0, 255, 0)  # rot
        sleep(1)
        for i in range(0, num_pixels):
            pixels[i] = (0, 0, 0)  # rot
        sleep(1)
        status_door = input("ROS::status door (1-Abbruch)?")
        if status_door == "1":
            break


def cont_red():
    while True:
        for i in range(0, num_pixels):
            pixels[i] = (0, 255, 0)  # rot
        status_door = input("ROS::status door (1-Abbruch)?")
        if status_door == "1":
            break


def cont_blue():
    while True:
        for i in range(0, num_pixels):
            pixels[i] = (0, 0, 255)  # rot
        status_door = input("ROS::status door (1-Abbruch)?")
        if status_door == "1":
            break


meas = input("Messung gestartet? (1)")
kuka_door = input("Start KUKA? (1)")

while meas == "1":
    cont_blue()
    if kuka_door == "1":
        blink_red()
        sleep(60)
        while True:
            cont_red()
            done = input("Kuka fertig? (1)")
            if done == "1":
                break
        blink_red()
        sleep(60)
    meas = input("Messung beendet? (0)")
    if meas != "1":
        break

print("Done")




