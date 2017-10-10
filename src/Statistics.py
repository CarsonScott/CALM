e = 2.718281828459

def logistic(x, a, b, c):
	return a / pow(e, -c*(x-b))

def gaussian(x, a, b, c):
	return a * pow(e, pow(x-b, 2) / (2*pow(c, 2)))

def quadratic(x, a, b, c):
	return a * pow(x, 2) + b*x + c