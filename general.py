from math import sqrt

class Vector:
	def __init__(self, x ,y):
		self.x = x
		self.y = y

	def normalize(self):
		x = self.x
		y = self.y
		
		if x == y == 0:
			return

		coef = sqrt(x ** 2 + y ** 2)

		self.mult_by_scalar(1 / coef)

	def mult_by_scalar(self, scalar):
		##print(self.x, self.y, scalar)
		assert(type(scalar) is int or type(scalar) is float)

		x = self.x
		y = self.y

		self.x *= scalar
		self.y *= scalar