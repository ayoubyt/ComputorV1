#!/usr/bin/python3.7

# this is the main page of our program
# for more info, check the readme file
from computer_v.main.read_equation import get_user_input, read_equation
from computer_v.math.polynomial import Polynomial
from computer_v.math.d2_polynomial import D2plynominal

#equation = read_equation()

p1 = Polynomial.fromexpr("(-2x + 4)-0.55x(x^2 + 5)")
p2 = D2plynominal.fromexpr("x^2 + 4 + 2x")

print(p1)
#print(p2)

#print(p1 ** 2)
