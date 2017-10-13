from math import sqrt
from MarkovNetwork import *
from BufferStore import *
from Statistics import *

class AdaptiveModel:

	def __init__(self, mSize, bSize):
		self.states = [0 for i in range(mSize)]
		self.memory = MarkovNetwork(mSize)
		self.buffer = BufferStore(bSize)
		self.lrate = 0.004
		self.drate = 0.001

	def update(self, x):
		v = self.buffer.add(x)
		if x != None: self.states[x] = 1
		if v != None: self.states[v] = 0
		
		data = self.buffer.data
		for i in range(len(data)):
			a = data[i]
			for j in range(len(self.states)):
				if j != a and None not in (a, j):
					m = self.memory.get(a, j)
					r = logistic(abs(m), 1, 0.5, -5)

					if self.states[j] == 1:
						m += self.lrate*r
					else:
						m -= self.drate*r

					self.memory.set(a, j, m)