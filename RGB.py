from microbit import *

for p in [pin2, pin1, pin8]:
    p.write_analog(0)

def rgb(rv, gv, bv, pins=[pin2, pin1, pin8]):
    r = pins[0]
    g = pins[1]
    b = pins[2]
    r.write_analog(rv)
    g.write_analog(gv)
    b.write_analog(bv)
