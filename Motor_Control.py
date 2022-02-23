import RPi.GPIO as GPIO
import time
from time import sleep

PUL_I = 11 # Motor 1 --> Tuergriff
DIR_I = 13 # Motor 1 Richtung

PUL_II = 29 # Motor 2 --> Tuerschwenker
DIR_II = 31 # Motor 2 Richtung

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PUL_I, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR_I, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PUL_II, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR_II, GPIO.OUT, initial=GPIO.LOW)

# Simulation ROS
open_door = input("ROS::open? ")

if open_door == "y":
    print("Tür auf läuft")
    GPIO.output(PUL_I, 1)
    GPIO.output(DIR_I, 1)
    sleep(5)
    GPIO.output(PUL_II, 1)
    GPIO.output(DIR_II, 1)
else:
    print("Fehler")


open_close = input("ROS::close? ")

if open_close == "y":
    print("Tür zu läuft")
    GPIO.output(PUL_I, 1)
    GPIO.output(DIR_I, 0)
    sleep(5)
    GPIO.output(PUL_II, 1)
    GPIO.output(DIR_II, 0)
else:
    print("Fehler")

GPIO.cleanup()