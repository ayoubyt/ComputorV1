#!/usr/bin/python3.7

# this is the main page of our program
# for more info, check the readme file
from computer_v.main.read_equation import get_user_input, read_equation
from computer_v.math.polynominal import Polynominal
from computer_v.math.d2_polynominal import D2Plynominal

#equation = read_equation()


p1 = Polynominal.fromexpr("x^2(x + 1)(2x +5.6) + (4 * 5 +6 /2 -4)")
p2 = D2Plynominal(1, 1, 1)

print(p2 / p1)

