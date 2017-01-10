from microbit import *

class display:
	def __init__(self, displayType='microbit'):
		if displayType == 'microbit':
			self.microbitDisplay()
		# else:
		# 	self.wifiDisplay()

	def getCurrentPos(self):
		return 'tr'

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
