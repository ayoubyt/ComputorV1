import sys
import re
from collections import deque

# eq stands for equation
def elemantary_validation(args):
	#check if num args is not one
	if (len(args) != 1):
		pae("usage: usage: python computor.py [-h] equation", 1)
	eq = args[0]
	# check for number of '='
	arr = list(args[0])
	n = arr.count("=")
	if (n != 1):
	 	pae("invalid equation, must be at least one and only one '=' sign", 1)
	# count number of variables
	vars = re.findall(r"[a-zA-Z]+", eq)
	if (len(set(vars)) != 1):
		pae("only one variable is allowed\nvars detected: {}.".format(set(vars)), 1)
	# detect invalid caracters
	ichars = re.findall(r"[^\w\s\+\-\*\/\=\^\(\)]", eq)
	if (len(ichars) > 0):
		pae("invalid characters\ninvalid characters detected: {}".format(ichars), 1)

"""
	this function is built to check the balance
	of brackets,'(' and ')' 
"""
def brackets_balance_validation(text):
	stack = deque()

	for l in text:
		if (l == '('):
			stack.append(l)
		elif (l == ')'):
			if (len(stack) == 0):
				pae("brackets are not well formated!", 1)
			stack.pop()
	if (len(stack) != 0):
		pae("brackets are not well formated!", 1)
		
#stands for print and exit
def pae(str, errno):
	print( "error: " + str, file=sys.stderr)
	sys.exit(errno)
