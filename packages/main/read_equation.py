import sys, getopt
from .validation import elemantary_validation, brackets_balance_validation
#TODO: kmmal read_equation nikmmk hh4


def read_equation():
	flags, args = get_user_input()
	#print (flags, args)
	elemantary_validation(args)
	equation = args[0]
	brackets_balance_validation(equation)

def get_user_input():
	try:
		flags, args = getopt.getopt(sys.argv[1:], "h", ["help"])
		return flags, args
	except getopt.GetoptError as err:
		print(err)
		sys.exit(2)
