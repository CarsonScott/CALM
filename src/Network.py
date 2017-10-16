#MIT License
#
#Copyright (c) 2017 Carson Scott
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

e = 2.718281828459

class Network:

	def compute(self, x):	
		return 1/(1 + pow(e, (x - self.bsize)))

	def __init__(self, msize, bsize):
		self.links = []
		self.states = []
		self.places = []
		self.msize = msize
		self.bsize = bsize
		self.lrate = 0.001
		self.drate = 0.0001
		for i in range(msize):
			self.links.append([])
			self.states.append(0)
			self.places.append(None)
			for j in range(msize):
				self.links[i].append(0)

	def update(self, x):
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
		total = 0
		for i in range(len(self.links)):
			if self.states[i] == 1:
				for j in range(len(self.links[i])):
					if len(y) == j: 
						y.append(0)
					v = self.links[i][j]
					d = v*(1-self.places[i]/self.bsize)
					y[j] += d
					total += d
		if total != 0:
			for i in range(len(y)):
				y[i] /= total
		return y