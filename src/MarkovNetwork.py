class MarkovNetwork:

	def __init__(self, size):
		self.data =[]

		for i in range(size):
			self.data.append([])
			for j in range(size):
				self.data[i].append(0)

	def get(self, i, j):
		if i > j:   return self.data[i][j]
		elif i < j: return self.data[j][i]
		return None

	def set(self, i, j, v):
		if i > j: self.data[i][j] = v
		if i < j: self.data[j][i] = v

