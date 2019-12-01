# the first letter of the function represents the algorithm or the method
# b : Babylonian method
# t : ternary operator

def bsqrt(number):
    """
        calculating square root using Babylonian method
        it's correct up to 14 after decimial
    """
    # first guess
    x = number
    # (number/<first guess> = 1)
    y = 1
    precision = 1e-15
    while (abs(x - y) / abs(x) > precision):
        x = (x + y) / 2
        y = number / x
    return round(x, 15)