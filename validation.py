from microbit import *
import radio

radio.on()
radio.config(channel = 26, address = 0x27182818)

msg = ["0 0", "0 0"]

def getValidDab(position):
    bend = [m[0] == 1 for m in msg]
    pitch = [m[2:] for m in msg]
    
    if position[1] == "l":
        if bend[0] or not bend[1]:
            return False
    else:
        if not bend[0] or bend[1]:
            return False
    
    if position[0] == "b":
        return pitch[0] > 20 and pitch[1] > 20
    else:
        return pitch[0] < -20 and pitch[1] < -20

while True:
    newMsg = radio.receive()
    if newMsg:
        newMsg = newMsg.split(" ")
        msg[0 if newMsg[0] == "L" else 1] = " ".join(newMsg[1:3])