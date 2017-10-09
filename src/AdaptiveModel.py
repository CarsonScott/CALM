from MarkovNetwork import *
from Buffer import *

def logistic(x, a, b, c):
	e = 2.718281828459
	return a / pow(e, -c*(x-b))

class AdaptiveModel:

	def __init__(self, mSize, bSize):
		self.memory = MarkovNetwork(mSize)
		self.buffer = Buffer(bSize)

	def update(self, x):
		self.buffer.add(x)
		data = self.buffer.data

		for i in range(len(data)):
			for j in range(i, len(data)):
				a = data[i]
				b = data[j]
				if a != b and None not in (a, b):
					v = self.memory.get(a, b)
					v += 0.001 * logistic(abs(v), 1, -1, 0)
					self.memory.set(a, b, v)

		data = self.memory.data
		for i in range(len(data)):
			for j in range(len(data)):
				x = self.memory.get(i, j)
				if x != None and x != 0:
					x -= 0.0001 * x/abs(x)
				self.memory.set(i, j, x)