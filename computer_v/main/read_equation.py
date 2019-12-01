import sys, getopt, re
from .validation import elemantary_validation, brackets_balance_validation
#TODO: kmmal read_equation nikmmk hh4


def read_equation():
	args = get_user_input()
	#print (flags, args)
	elemantary_validation(args)
	equation = args[0]
	brackets_balance_validation(equation)
	return (equation)
	#get the variable bnanme

	#return(equation)

def get_user_input():
	# try:
	# 	flags, args = getopt.getopt(sys.argv[1:], "h", ["help"])
	# 	return flags, args
	# except getopt.GetoptError as err:
	# 	print(err)
	# 	sys.exit(2)
	return sys.argv[1:]
