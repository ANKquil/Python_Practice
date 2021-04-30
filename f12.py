def f12(x):
    if x < -27:
        sum0 = 32*x**4 + 47*x**6 + 92
    else:
        if -27 <= x < 40:
            sum0 = 79*x**6 + x + 6
        else:
            if x >= 40:
                sum0 = 86*x**8 - 64*x + 75
    return sum0
