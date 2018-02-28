from microbit import *

import radio
import random
import music

radio.on()
radio.config(channel = 26, address = 0x27182818)

currentCombinedPosition = ["0 0", "0 0"]

position_to_image = {
    'tl': Image.ARROW_NW,
    'tr': Image.ARROW_NE,
    'bl': Image.ARROW_SW,
    'br': Image.ARROW_SE
}

positions = [key for key in position_to_image.keys()]
currentPosition = positions[0]
lastTime = running_time()

timeDif = 2000

def getRandomPosition():
    return random.choice(positions)

def getNextDab(position):
    availablePositions = positions[:]
    availablePositions.remove(position)
    return random.choice(availablePositions)
        

def getValidDab(position, combinedPosition):
    bend = [m[0] == "1" for m in combinedPosition]
    pitch = [0, 0]

    try:
        pitch = [float(m[2:]) for m in combinedPosition]
    except ValueError:
        return True
    
    #if position[1] == "l":
    #    if bend[0] or not bend[1]:
    #        return False
    #else:
    #    if not bend[0] or bend[1]:
    #        return False
    
    if position[0] == "t":
        return pitch[0] > 20 and pitch[1] > 20
    else:
        return pitch[0] < -20 and pitch[1] < -20


def getNewDabMessage():
    try:
        newMsg = radio.receive()
        return newMsg
    except Exception as e:
        #Removes the radio messages that were causing it to crash
        radio.receive_bytes()

def updateCurrentCombinedPosition(newMsg):
    newMsg = newMsg.split(" ")
    currentCombinedPosition[0 if newMsg[0] == "L" else 1] = " ".join(["0", newMsg[-1]])  

while True:
    # message is of format "{side} {isBent} {pitch}"
    newMsg = getNewDabMessage()

    display.show(position_to_image[currentPosition])
    
    if newMsg and isinstance(newMsg, str):
        updateCurrentCombinedPosition(newMsg)

    if running_time() - lastTime > timeDif:
        print('currentCombinedPosition: ', currentCombinedPosition)
        if getValidDab(currentPosition, currentCombinedPosition):
            print("tick")
            timeDif = max(500, timeDif - 50)
        else:
            print("cross")
        lastTime = running_time()
        
        currentPosition = getNextDab(currentPosition)
        print(currentPosition)