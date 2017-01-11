from microbit import *
import music
import random

while True:
  
  music.play(music.NYAN, loop=True, wait=False)
  
  if getValidDab():
    music.play(music.POWER_UP)
  else:
    music.play(music.POWER_DOWN)
    
