import time
from time import sleep

PUL_I = 11  # Motor 1 --> Tuergriff
DIR_I = 13  # Richtung

PUL_II = 29  # Motor 2 --> Tuerschwenker
DIR_II = 31  # Richtung

def door_open(door_op):
    LS1G = input("Sensor1 'geschlossen' (1)")  # Türgriff "geschlossen" Sensor
    LS2G = input("Sensor2 'geschlossen' (1)")  # Türschwenker "geschlossen" Sensor

    if door_op == LS1G == LS2G == "1":

        while LS1G == "1":
            print("Griff 1 läuft")
            open_griff = input("Sensor1 'offen' (1)")  # Türgriff "offen" Sensor
            sleep(1)
            if open_griff == "1":
                break
        print("Türgriff offen")

        sleep(5)

        while LS2G == "1":
            print("Schwenker 1 läuft")
            open_schwenker = input("Sensor2 'offen' (1)")  # Türgriff "geschlossen" Sensor
            sleep(1)
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
    LS1O = input("Sensor1 'offen' (1)")  # Türgriff "offen" Sensor
    LS2O = input("Sensor2 'offen' (1)")  # Türschwenker "offen" Sensor

    if door_cl == LS1O == LS2O == "1":

        while LS1O == "1":
            print("Griff 2 läuft")
            close_griff = input("Sensor1 'geschlossen' (1)")  # Türgriff "geschlossen" Sensor
            sleep(1)
            if close_griff == "1":
                break
        print("Türgriff geschlossen")

        sleep(5)

        while LS2O == "1":
            print("Schwenker 2 läuft")
            close_schwenker = input("Sensor2 'geschlossen' (1)")  # Türschwenker "geschlossen" Sensor
            sleep(1)
            if close_schwenker == "1":
                break
        print("Türgriff offen")
        status_closed = 1
    else:
        status_closed = 0
        print("Door is already closed")

        return status_closed


door = input("Open door (1) / Close door (2)")

if door == "1":
    door_open(door)
else:
    door_close(door)
