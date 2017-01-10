# required for position selection
import random

# detects positions (not yet)
class dabtector:
	def __init__(self):
		self.positions = ['tl', 'tr', 'bl', 'br']
		self.axis = ['x', 'y', 'z']

# holds the default positions after calibration
class positions:
	def __init__(self):
		self.positions = ['tl', 'tr', 'bl', 'br']
		self.axis = ['x', 'y', 'z']
		# dictionary to store accelerometer values
		self.accel = {'tr':{'x': 0, 'y': 0, 'z': 0}, 'tl':{'x': 0, 'y': 0, 'z': 0}, 'br':{'x': 0, 'y': 0, 'z': 0}, 'bl':{'x': 0, 'y': 0, 'z': 0}}
		# dictionary to store compass values
		self.compass = {'tr':{'x': 0, 'y': 0, 'z': 0}, 'tl':{'x': 0, 'y': 0, 'z': 0}, 'br':{'x': 0, 'y': 0, 'z': 0}, 'bl':{'x': 0, 'y': 0, 'z': 0}}

		self.accelRange = {}
		self.compassRange = {}

	# allows the defaults to be pushed to the dictionaries for calling later
	# position: ['tl', 'tr', 'bl', 'br']
	# values: [accel-x, accel-y, accel-z, compass-x, compass-y, compass-z]
	def calibrate(self, position, values):
		# checks that the position exists in the dictionary (causes errors)
		if position in self.accel.keys() and position in self.compass.keys():
			# stores the axis is
			axisCounter = 0
			# set accelerometer values
			for axis in self.accel[position].keys():
				self.accel[position][axis] = values[axisCounter]
				axisCounter += 1

			# set compass values
			for axis in self.compass[position].keys():
				self.compass[position][axis] = values[axisCounter]
				axisCounter += 1

	def dictcw(self, move):
		if move == 'tr':
			return 'br'
		elif move == 'br':
			return 'bl'
		elif move == 'bl':
			return 'tl'
		elif move == 'tl':
			return 'tr'

	def dictccw(self, move):
		if move == 'tr':
			return 'tl'
		elif move == 'tl':
			return 'bl'
		elif move == 'bl':
			return 'br'
		elif move == 'br':
			return 'tr'

	def movementRanges(self):
		for move in self.positions:
			self.accelRange[move] = {}
			for axis in self.axis:
				dabrangelow = (self.accel[self.dictccw(move)][axis] + self.accel[move][axis]) // 2
				dabrangehigh = (self.accel[self.dictcw(move)][axis] + self.accel[move][axis]) // 2
				self.accelRange[move][axis] = [dabrangelow, dabrangehigh]

class moves:
	def __init__(self):
		self.positions = ['tl', 'tr', 'bl', 'br']
		self.axis = ['x', 'y', 'z']
		self.currentMove = ''

	def next(self):
		# randomly selects the next position for the user
		self.currentMove = random.choice(self.positions)
		return self.currentMove

	def check(self, current):
		pos = positions()
		for pos in self.positions:
			for axis in self.axis:
				dabRange = pos.accelRange[pos][axis]
				dabRange = range(dabRange[0], dabRange[1])
				if current in dabRange:
					return True
				else:
					return False

# calls the dabtector class for use under the variable 'dabtector'
dabtector = dabtector()

# calls the positions call for use under the variable 'pos'
pos = positions()

# sets the top right ('tr') position to the values given (accel-x, accel-y, accel-z, compass-x, compass-y, compass-z)
pos.calibrate('tr', [10, 20, 30, 40, 50, 60])

# prints the x value of the accelerometer at top right (tr)
# print(pos.accel['tr']['x'])

pos.movementRanges()

print(pos.accelRange)