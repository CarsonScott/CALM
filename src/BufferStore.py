class BufferStore:

	def __init__(self, size):
		self.data = []
		for i in range(size):
			self.data.append(None)

	def add(self, x):
		self.data.insert(0, x)
		y = self.data[len(self.data)-1]
		del self.data[len(self.data)-1]
		return y

