from microbit import *
import math
    
def getPitch():
    x = accelerometer.get_x() / 1024
    y = accelerometer.get_y() / 1024
    z = accelerometer.get_z() / 1024
    
    return math.degrees(math.atan(y/((math.sqrt(x**2 + z**2) if math.sqrt(x**2 + z**2) != 0 else 0.1))))
    
def getValidDab(position):
    if position[0] == "b":
        return getPitch() > 20
    else:
        return getPitch() < -20
