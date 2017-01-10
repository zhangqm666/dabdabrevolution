# detects positions (not yet)
class dabtector:
	def __init__(self):
		self.positions = ['tl', 'tr', 'bl', 'br']

# holds the default positions after calibration
class positions:
	def __init__(self):
		# dictionary to store accelerometer values
		self.accel = {'tr':{'x': 0, 'y': 0, 'z': 0}, 'tl':{'x': 0, 'y': 0, 'z': 0}, 'br':{'x': 0, 'y': 0, 'z': 0}, 'bl':{'x': 0, 'y': 0, 'z': 0}}
		# dictionary to store compass values
		self.compass = {'tr':{'x': 0, 'y': 0, 'z': 0}, 'tl':{'x': 0, 'y': 0, 'z': 0}, 'br':{'x': 0, 'y': 0, 'z': 0}, 'bl':{'x': 0, 'y': 0, 'z': 0}}

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

# calls the dabtector class for use under the variable 'dabtector'
dabtector = dabtector()

# calls the positions call for use under the variable 'pos'
pos = positions()

# sets the top right ('tr') position to the values given (accel-x, accel-y, accel-z, compass-x, compass-y, compass-z)
pos.calibrate('tr', [10, 20, 30, 40, 50, 60])

# prints the x value of the accelerometer at top right (tr)
print(pos.accel['tr']['x'])