import string

class TrackPoint(object):
	def __init__(self, name):
		self.name = name
		self.left = None
		self.right = None
		self.straight = None

		self.lazy = True
		self.leftNext = True
	
	def inFromLeft(self):
		if self.lazy:
			self.leftNext = True

		return self.straight

	def inFromRight(self):
		if self.lazy:
			self.leftNext = False

		return self.straight

	def inFromStraight(self):
		if self.leftNext:
			toreturn = self.left
		else:
			toreturn = self.right

		if not self.lazy:
			self.leftNext = not self.leftNext

		return toreturn

	def inFrom(self, other):
		if other == self.left:
			return self.inFromLeft()
		elif other == self.right:
			return self.inFromRight()
		elif other == self.straight:
			return self.inFromStraight()
	
	def connect(first, firstside, second, secondside):
		first.__setattr__(firstside, second)
		second.__setattr__(secondside, first)

	def isConnected(self):
		return self.straight and self.left and self.right

def makeMap():
	P = {}

	for letter in string.uppercase[:-2]:
		P[letter] = TrackPoint(letter)

	#Top row
	P['A'].connect('left',     P['E'], 'straight')
	P['A'].connect('right',    P['F'], 'straight')
	P['B'].connect('left',     P['G'], 'straight')
	P['B'].connect('right',    P['H'], 'straight')
	P['C'].connect('left',     P['I'], 'straight')
	P['C'].connect('right',    P['J'], 'straight')
	P['D'].connect('left',     P['K'], 'straight')
	P['D'].connect('right',    P['L'], 'straight')

	P['A'].connect('straight', P['D'], 'straight')
	P['B'].connect('straight', P['C'], 'straight')

	#Bottom row
	P['U'].connect('left',     P['M'], 'straight')
	P['U'].connect('right',    P['N'], 'straight')
	P['V'].connect('left',     P['O'], 'straight')
	P['V'].connect('right',    P['P'], 'straight')
	P['W'].connect('left',     P['Q'], 'straight')
	P['W'].connect('right',    P['R'], 'straight')
	P['X'].connect('left',     P['S'], 'straight')
	P['X'].connect('right',    P['T'], 'straight')

	P['U'].connect('straight', P['V'], 'straight')
	P['W'].connect('straight', P['X'], 'straight')

	#Middle rows
	P['E'].connect('left',     P['M'], 'right')
	P['E'].connect('right',    P['N'], 'left')
	P['F'].connect('left',     P['N'], 'right')
	P['F'].connect('right',    P['O'], 'left')
	P['G'].connect('left',     P['O'], 'right')
	P['G'].connect('right',    P['P'], 'left')
	P['H'].connect('left',     P['P'], 'right')
	P['H'].connect('right',    P['Q'], 'left')
	P['I'].connect('left',     P['Q'], 'right')
	P['I'].connect('right',    P['R'], 'left')
	P['J'].connect('left',     P['R'], 'right')
	P['J'].connect('right',    P['S'], 'left')
	P['K'].connect('left',     P['S'], 'right')
	P['K'].connect('right',    P['T'], 'left')
	P['L'].connect('left',     P['T'], 'right')
	P['L'].connect('right',    P['M'], 'left')

	for name, point in P.iteritems():
		assert point.isConnected(), "%s is not connected" % name
	
	return P

flipflop = list(raw_input("Flip flop points: ").upper())
last, at = list(raw_input("Moving along: ").upper())
count = int(raw_input("Iterations: "))

points = makeMap()

for letter in flipflop:
	points[letter].lazy = False

last = points[last]
at = points[at]

passed = []

for i in range(count):
	#passed += [at.name]
	next = at.inFrom(last)
	last = at
	at = next

#print ''.join(passed)
print last.name+at.name
