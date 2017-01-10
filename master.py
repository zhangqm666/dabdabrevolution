# master microbit

# imports
from microbit import *
import radio
import random

radio.on()
radio.config(channel = 26, address = 0x27182818)

class master:
	def __init__(self):
		self.positions = ['tl', 'tr', 'bl', 'br']
		self.axis = ['x', 'y', 'z']
		self.currentMove = ''
		self.playerDab = ''

	def next(self):
		# randomly selects the next position for the user
		self.currentMove = random.choice(self.positions)
		return self.currentMove

	def getDab(self):
		dab = radio.receive()
		if dab:
			self.playerDab = dab

	def checkDab(self):
		timelen = running_time()
		while timelen < 3000:
			self.getDab()
			if self.playerDab == self.currentMove:
				return True
		return False

class run:
	def __init__(self):
		self.master = master()
		self.display = display()

	def play(self):
		while True:
			self.master.next()
			self.master.checkDab()
			sleep(500)

class display:
	def __init__(self, displayType='microbit'):
		if displayType == 'microbit':
			self.microbitDisplay()
		# else:
		# 	self.wifiDisplay()

	def getCurrentPos(self):
		master = master()
		return master.currentMove

	# get current position (generated) and displays on the 5x5 display
	def microbitDisplay(self):
		while True:
			currentPos = self.getCurrentPos()
			imageToDisplay = None
			if currentPos == 'tl':
				imageToDisplay = Image.ARROW_NW
			elif currentPos == 'tr':
				imageToDisplay = Image.ARROW_NE
			elif currentPos == 'bl':
				imageToDisplay = Image.ARROW_SW
			elif currentPos == 'br':
				imageToDisplay = Image.ARROW_SE

			if imageToDisplay == None:
				display.clear()
			else:
				display.show(imageToDisplay)



