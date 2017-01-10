from microbit import *
import math
import radio

side = "L"

radio.on()
radio.config(channel = 26, address = 0x27182818)

def isBent(calib_read):
    return abs(calib_read - pin0.read_analog()) > 60

def getPitch():
    x = accelerometer.get_x() / 1024
    y = accelerometer.get_y() / 1024
    z = accelerometer.get_z() / 1024
    
    return math.degrees(math.atan(y/((math.sqrt(x**2 + z**2) if math.sqrt(x**2 + z**2) != 0 else 0.1))))

def switchSide():
    side = "R" if side == "L" else "L"

while True:
    if button_a.was_pressed():
        switchSide()
    display.show(side)
    radio.send(side, ("1" if isBent() else "0"), str(getPitch()))