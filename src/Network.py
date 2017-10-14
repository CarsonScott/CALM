e = 2.718281828459

class Network:

	def compute(self, x):	
		return 1/(1 + pow(e, (x - self.bsize)))

	def __init__(self, msize, bsize):
		self.pred = []
		self.links = []
		self.states = []
		self.places = []
		self.msize = msize
		self.bsize = bsize
		self.lrate = 0.0002
		self.drate = 0.0001
		self.thresh = 0.025
		for i in range(msize):
			self.pred.append(0)
			self.links.append([])
			self.states.append(0)
			self.places.append(None)
			for j in range(msize):
				self.links[i].append(0)

	def update(self, x):
		y = None
		for i in range(len(self.states)):
			if self.states[i] == 1:
				if self.places[i] >= self.bsize:
					self.places[i] = None
					self.states[i] = 0
				else:
					d = self.compute(self.places[i])
					self.links[i][x] += self.lrate*d
					if self.links[i][x] > 1: 
						self.links[i][x] = 1
					self.places[i] += 1
			else:
				self.links[i][x] -= self.drate
				if self.links[i][x] < 0: 
					self.links[i][x] = 0

		self.states[x] = 1
		self.places[x] = 0

	def predict(self):
		y = []
		for i in range(len(self.links)):
			if self.states[i] == 1:
				for j in range(len(self.links[i])):
					if len(y) == j: 
						y.append(0)
					v = self.links[i][j]
					y[j] += v*(1-self.places[i]/self.bsize)
				y[j] /= self.bsize

		return y
