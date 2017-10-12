from math import sqrt
e = 2.718281828459


class Network:
	
	def compute(self, x):	
		return 1/pow(e, 0.5 * (x - 0.1))

	def __init__(self, mSize, bSize):
		self.links = []
		self.states = []
		self.places = []
		self.msize = mSize
		self.bsize = bSize
		self.lrate = 0.0004
		self.drate = 0.0001

		for i in range(mSize):
			self.links.append([])
			self.states.append(0)
			self.places.append(None)

			for j in range(mSize):
				self.links[i].append(0)

	def update(self, x):
		for i in range(len(self.states)):
			if self.states[i] == 1:
				self.places[i] += 1
				if self.places[i] >= self.bsize:
					self.places[i] = None
					self.states[i] = 0
				else:
					d = self.compute(self.places[i])
					self.links[i][x] += self.lrate*d
			else:
				self.links[i][x] -= self.drate
			if abs(self.links[i][x]) > 1:
				self.links[i][x] /= abs(self.links[i][x])
		self.states[x] = 1
		self.places[x] = 0