from microbit import *

# is flex sensor bent?
def is_bent(calib_read, present_read):
    if abs(calib_read - present_read) > 60:
        return True
    return False

# print analog readings
while True:
    a = pin2.read_analog()
    print(a)
    sleep(500)
    
# calib_read is normally:
# 796, 812, 650, 630, 797, 830

# present_read is normally:
# ###, ###, 963, ###, 658