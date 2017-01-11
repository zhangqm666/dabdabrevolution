from microbit import *

pins = [pin2, pin1, pin8]

for p in pins:
    p.write_analog(0)

r = pins[0]
g = pins[1]
b = pins[2]

while True:
    r.write_analog(1023) # r
    g.write_analog(0) # g
    b.write_analog(0) # b