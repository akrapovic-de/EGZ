import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Init motors
PUL_I = 11  # Motor 1 --> Tuergriff
DIR_I = 13  # Motor 1 Richtung

PUL_II = 29  # Motor 2 --> Tuerschwenker
DIR_II = 31  # Motor 2 Richtung

GPIO.setup(PUL_I, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR_I, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PUL_II, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR_II, GPIO.OUT, initial=GPIO.LOW)

# Init sensors
handle1 = 1
handle2 = 2
swing1 = 3
swing2 = 4
stop1 = 5
stop2 = 6

GPIO.setup(handle1, GPIO.IN, initial=GPIO.LOW)
GPIO.setup(handle2, GPIO.IN, initial=GPIO.LOW)
GPIO.setup(swing1, GPIO.IN, initial=GPIO.LOW)
GPIO.setup(swing2, GPIO.IN, initial=GPIO.LOW)
GPIO.setup(stop1, GPIO.IN, initial=GPIO.LOW)
GPIO.setup(stop2, GPIO.IN, initial=GPIO.LOW)


def door_open(door_op):
    LS1G = GPIO.IN(handle1)
    LS2G = GPIO.IN(swing1)

    door_op = 1

    if door_op == LS1G == LS2G == 1:

        while LS1G == "1":
            print("Griff 1 läuft")
            GPIO.output(PUL_I, 1)
            GPIO.output(DIR_I, 1)
            open_griff = GPIO.IN(handle2)
            sleep(0.5)
            if open_griff == "1":
                break
        print("Türgriff offen")

        sleep(2)

        while LS2G == "1":
            print("Schwenker 1 läuft")
            GPIO.output(PUL_II, 1)
            GPIO.output(DIR_II, 1)
            open_schwenker = GPIO.IN(swing2)
            sleep(0.5)
            if open_schwenker == "1":
                break
        print("Türschwenker offen")
        print("Door is open")
        status_open = 1
    else:
        status_open = 0
        print("Door is already open")

        return status_open


def door_close(door_cl):
    LS1O = GPIO.IN(handle2)
    LS2O = GPIO.IN(swing2)

    door_cl = 1

    if door_cl == LS1O == LS2O == 1:

        while LS1O == "1":
            print("Griff 2 läuft")
            GPIO.output(PUL_I, 0)
            GPIO.output(DIR_I, 0)
            closed_griff = GPIO.IN(handle1)
            sleep(0.5)
            if closed_griff == "1":
                break
        print("Türgriff offen")

        sleep(2)

        while LS2O == "1":
            print("Schwenker 2 läuft")
            GPIO.output(PUL_II, 0)
            GPIO.output(DIR_II, 0)
            closed_schwenker = GPIO.IN(swing1)
            sleep(0.5)
            if closed_schwenker == "1":
                break
        print("Türgriff offen")
        status_closed = 1
    else:
        status_closed = 0
        print("Door is already closed")

        return status_closed


door = input("Open door (open) / Close door (close)")

if door == "open":
    door_open(door)
elif door == "close":
    door_close(door)
else:
    print("Error")

GPIO.cleanup()
