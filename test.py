#!/usr/bin/python3.7
import re

from collections import deque

import pandas

class Emp:
	def __init__(self, name, lastname):
		self.name = name
		self.lastname = lastname

	@classmethod
	def fromstring(cls, str):
		s = str.split(" ")
		return (cls(s[0], s[1]))

	@staticmethod
	def f(str):
		s = str.split(" ")
		return (Emp(s[0], s[1]))


msnaoi = Emp.f("anass msnaoiu")

print(msnaoi.name)
