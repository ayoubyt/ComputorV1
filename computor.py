#!/usr/bin/env python3

# this is the main page of our program
# for more info, check the readme file
import re
from computer_v.main.read_equation import get_user_input, read_equation
from computer_v.math.polynomial import Polynomial, D2plynominal, D1plynominal
import computer_v.glob as g

try:
    equation = read_equation()
#parisng var name
    g.varname = re.search(r"[a-zA-Z]+", equation).group(0)
    equation = re.sub(r"[a-zA-Z]+", "x", equation)
    left, right = equation.split("=")

    eq_poly = Polynomial.fromexpr(left) - Polynomial.fromexpr(right)

    if (eq_poly.deg == 2):
        D2plynominal(eq_poly.coefs).solve()
    elif (eq_poly.deg == 1):
        D1plynominal(eq_poly.coefs).solve()
    elif (eq_poly.deg == 0):
        if (eq_poly.coefs[0] == 0):
            print("all numbers are solutions to this eqation")
        else:
            print("equation has no solution")
    else:
        print(eq_poly, "= 0")
        print(f"equations of degree 3 or higher are not supported")
except Exception as e:
    print(e)

#TODO ./computor.py "-10 = -1(x^2 + 0)"
