from microbit import *
import math
import radio

side = "L"
calib_read = 0

radio.on()
radio.config(channel = 26, address = 0x27182818)

def isBent(calib_read):
    return calib_read > pin2.read_analog()

def getPitch():
    x = accelerometer.get_x() / 1024
    y = accelerometer.get_y() / 1024
    z = accelerometer.get_z() / 1024
    
    return math.degrees(math.atan(y/((math.sqrt(x**2 + z**2) if math.sqrt(x**2 + z**2) != 0 else 0.1))))

def switchSide(side):
    return "R" if side == "L" else "L"

while True:
    if button_a.was_pressed():
        side = switchSide(side)
    if button_b.was_pressed():
        calib_read = pin2.read_analog()
    display.show(side)
    radio.send(str(side + " " + ("1" if isBent(calib_read) else "0") + " " + str(getPitch())))
    sleep(100)