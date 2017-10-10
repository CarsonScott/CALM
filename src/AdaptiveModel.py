from math import sqrt
from MarkovNetwork import *
from BufferStore import *
from Stats import gaussian, quadratic

class AdaptiveModel:

	def __init__(self, mSize, bSize):
		self.memory = MarkovNetwork(mSize)
		self.buffer = BufferStore(bSize)
		self.lrate = 0.001
		self.drate = 0.0006

	def update(self, x):
		self.buffer.add(x)
		data = self.buffer.data
		for i in range(len(data)):
			for j in range(i, len(data)):
				a = data[i]
				b = data[j]
				if a != b and None not in (a, b):
					v = self.memory.get(a, b)
					v += self.lrate * logistic(abs(v), 1, 0, -1) * sqrt(abs(a-b))
					self.memory.set(a, b, v)

		data = self.memory.data
		for i in range(len(data)):
			for j in range(len(data)):
				x = self.memory.get(i, j)
				if x != None:
					x -= self.drate * quadratic(x, 1, 0, .1)			
					if abs(x) > 1:
						x = x/abs(x)	
					self.memory.set(i, j, x)