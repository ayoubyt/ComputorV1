import sys
import getopt
import re
from .validation import elemantary_validation, brackets_balance_validation
# TODO: kmmal read_equation nikmmk hh4


def read_equation():
    args = get_user_input()
    elemantary_validation(args)
    equation = args[0]
    brackets_balance_validation(equation)
    return (equation)


def get_user_input():
    try:
        flags, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        flags = [e[0] for e in flags]
        if (len(flags) > 0):
            if "-h" in flags:
                print("""usage: python computor.py [-h] equation

example: python computor.py '2x^2 +1 = -3'
				""")
                exit(0)
        return args
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
