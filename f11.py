import math


def f11(x):
    sum1 = (32 * (x*x*x*x)) + (47 * (x*x*x*x*x*x)) + 92
    sum2 = (79 * (x ** 6)) + x + 6
    sum3 = sum1/sum2
    # sum4 = log(x) - log(x) =  0
    sum5 = (x ** 2) - (71 * x) + 98
    sum6 = math.sin(x) + (x**4) - 84
    sum7 = sum5 / sum6
    sum7 = math.sqrt(sum7)
    sum0 = sum3 - sum7
    return sum0
