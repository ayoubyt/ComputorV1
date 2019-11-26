#import numpy as np
import re
from collections import deque

class Polynominal:
	"""
		polynominal class respresents aplonominal hh
		you initiaise it by in inputing an array of the coefficients of tha polynomanal ordered from left to right
		ex: 1 + 5x + 2x^2 --> plonominal([1, 5, 2])
	"""
	def __init__(self, coefficients):
		self.coefs = self.__trim_coefs(coefficients)

	def __trim_coefs(self, coefs):
		"""
			__trim_coef is privat function designed to remove all
			the nonsense zeros that the user inputs at the end of the array of coefficients
		"""
		while (len(coefs) > 0 and coefs[-1] == 0):
			coefs.pop()
		return (coefs)

	def __str__(self):
		res = ""
		if (len(self.coefs) < 1):
			return ("0")
		for i, co in enumerate(self.coefs):
			if (co != 0):
				co = co if isinstance(co, int) else float("%.2f" % co)
				if (i > 0):
					if (co != 1):
						res += str(co)
					res += "x^%d" % i
				else:
					res += str(co)
				if (i < len(self.coefs) - 1):
					res += " + "
		return res

	def __add__(self, other):
		p1 = self.coefs
		p2 = other.coefs
		if (len(p2) > len(p1)):
			p1, p2 = p2, p1
		for i, co in enumerate(p2):
			p1[i] += co
		return (Polynominal(p1))

	def __sub__(self, other):
		p1 = self.coefs
		p2 = other.coefs
		if (len(p2) > len(p1)):
			p1, p2 = p2, p1
		for i, co in enumerate(p2):
			p1[i] -= co
		return (Polynominal(p1))

	def __mul__ (self, other):
		p1 = self.coefs
		p2 = other.coefs
		l = len(p1) + len(p2) - 2
		result = [0] * (l + 1)
		for i in range(l + 1):
			for j in range(i + 1):
				result[i] += (p1[j] if j < len(p1) else 0) * (p2[i - j] if i - j < len(p2) else 0)
		return Polynominal(self.__trim_coefs(result))

	@classmethod
	def parse_to_plynomainals(cls, str):
		pass

	@classmethod
	def fromexpr(cls, expr):
		#this function transform an arrays of elements to a deque


		#remove whitespacecs
		expr = re.sub(r"\s", "", expr)
		#hh i think there is some thing better
		#expr = re.sub(r"([a-zA-Z]|\)|\d)(\(|[a-zA-Z]|\d)", r"\1*\2", expr)
		match = re.finditer(r"(?=(([a-zA-Z]|\)|\d+(\.\d+)?)(\(|[a-zA-Z]|\d+(\.\d+)?)))", expr)
		for e in match:
			print(e.group())
		# print("expr = ", expr)
		elements = re.finditer(r"(\d+(\.\d+)?|[a-zA-Z]+|[\+\*\/\-\^\(\)])", expr)
		# print(elements)
		#print(cls._to_postfix(elements))

	@classmethod
	def _to_postfix(cls, arr):
		"""
			takes an array of elements of an expression
			an returns a queue of elemts represents a postfix
			notation of the first expresstion
		"""
		ops = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
		opstack = deque()
		output = []
		for c in arr:
			if (c.isdigit()):
				output.append(Polynominal([float(c)]))
			if c in ops:
				if (len(opstack) > 0):
					if (ops[c] < ops[opstack[-1]]):
						output.append(opstack.pop())
					elif (ops[c] == ops[opstack[-1]]):
						if (c != "^"):
							output.append(opstack.pop())
				opstack.append(c)
			if (c in "()"):
				if (c == "("):
					opstack.append(c)
				else:
					while (len(opstack) > 0):
						tmp = opstack.pop()
						if (tmp == "("):
							break
						else:
							output.append(c)
		while(len(opstack) > 0):
			output.append(opstack.pop())
		return(output)
					


	#def __pow__(self, other):
