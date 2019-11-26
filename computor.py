#!/usr/bin/python3.7

# this is the main page of our program
# for more info, check the readme file
from packages.main.read_equation import get_user_input, read_equation
from packages.math.polynominals import Polynominal

#equation = read_equation()
Polynominal.fromexpr("-x + x * 2")
