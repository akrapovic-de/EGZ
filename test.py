import time
from time import sleep

PUL_I = 11  # Motor 1 --> Tuergriff
DIR_I = 13  # Richtung

PUL_II = 29  # Motor 2 --> Tuerschwenker
DIR_II = 31  # Richtung


def door_open(door_op):
    LS1G = input("Sensor1 'geschlossen' (1)")  # Türgriff "geschlossen" Sensor
    LS2G = input("Sensor2 'geschlossen' (1)")  # Türschwenker "geschlossen" Sensor

    door_op = "1"

    if door_op == LS1G == LS2G == "1":

        while LS1G == "1":
            print("Griff 1 läuft")
            open_griff = input("Sensor1 'offen' (1)")  # Türgriff "offen" Sensor
            sleep(0.5)
            if open_griff == "1":
                break
        print("Türgriff offen")

        sleep(1)

        while LS2G == "1":
            print("Schwenker 1 läuft")
            open_schwenker = input("Sensor2 'offen' (1)")  # Türgriff "geschlossen" Sensor
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
    LS1O = input("Sensor1 'offen' (1)")  # Türgriff "geschlossen" Sensor
    LS2O = input("Sensor2 'offen' (1)")  # Türschwenker "geschlossen" Sensor

    door_cl = "1"

    if door_cl == LS1O == LS2O == "1":

        while LS2O == "1":
            print("Schwenker 1 läuft")
            closed_schwenker = input("Sensor2 'geschlossen' (1)")  # Türgriff "geschlossen" Sensor
            sleep(0.5)
            if closed_schwenker == "1":
                break
        print("Türschwenker zu")

        sleep(1)

        while LS1O == "1":
            print("Griff 1 läuft")
            closed_griff = input("Sensor1 'geschlossen' (1)")  # Türgriff "offen" Sensor
            sleep(0.5)
            if closed_griff == "1":
                break
        print("Türgriff zu")
        print("Door is closed")
        status_open = 1
    else:
        status_open = 0
        print("Door is already closed")

        return status_open


door = input("Open door (open) / Close door (close)")

if door == "open":
    door_open(door)
elif door == "close":
    door_close(door)
else:
    print("Error")
