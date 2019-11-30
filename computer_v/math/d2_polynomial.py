from .polynomial import Polynomial

class D2plynominal(Polynomial):

	"""
		2d Polynomial represents a second degree Polynomial
		d2Polynominal(c, b, a) when (a, b ,c) represents the coefficient of
		the Polynomial a * x^2 + b * x + c   	
	"""

	def __init__(self, c, b, a):
		super().__init__([c, b, a])

	@classmethod
	def fromexpr(cls, expr):
		result = Polynomial.fromexpr(expr)
		if (result.deg > 2):
			raise cls.PolynominalError("affecting polynomial with deg more than two to deg two polynomial")
		else:
			co = result.coefs
			return cls(co[0], co[1], co[2])
		#print(Error)

	
