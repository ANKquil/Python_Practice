import math


def f14(x):
    if x == 0:
        sum0 = 4
    elif x == 1:
        sum0 = 3
    else:
        sum0 = math.tan(f14(x - 1)) - math.cos(f14(x - 1))
    return sum0
