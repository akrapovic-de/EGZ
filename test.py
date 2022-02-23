PUL_I = 11 # Motor 1 --> Tuergriff
DIR_I = 13 # Richtung

PUL_II = 29 # Motor 2 --> Tuerschwenker
DIR_II = 31 # Richtung

# Simulation ROS
open_door = input("ROS::open? (y/n) ")

if open_door == "y":
    print("M1 läuft")
else:
    print("M1 Fehler")

open_close = input("ROS::close? (y/n) ")

if open_close == "y":
    print("M2 läuft")
else:
    print("M2 Fehler")
