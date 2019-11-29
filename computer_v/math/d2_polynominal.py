from .polynominal import Polynominal

class D2Plynominal(Polynominal):

	"""
		2d polynominal represents a second degree polynominal
		d2Polynominal(c, b, a) when (a, b ,c) represents the coefficient of
		the polynominal a * x^2 + b * x + c   	
	"""

	def __init__(self, c, b, a):
		super().__init__([c, b, a])
		#print(Error)

	
