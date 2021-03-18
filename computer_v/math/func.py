def bsqrt(number):
    x = number
    y = 1
    precision = 1e-15
    while (abs(x - y) / abs(x) > precision):
        x = (x + y) / 2
        y = number / x
    return round(x, 15)
