from microbit import *

count = 0

while True:
    if button_a.was_pressed():
        count += 1
        display.scroll(str(count), wait = False, loop = True)
    if button_b.was_pressed():
        count = 0
        display.clear()