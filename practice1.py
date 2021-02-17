from math import sin, sqrt, tan, cos


def print_finish_num(x):
    print("{:1.2e}".format(x))


def practice1():
    x = float(input())
    sum1 = 32 * x ** 4 + 47 * x ** 6 + 92
    sum2 = 79 * x ** 6 + x + 6
    sum3 = sum1 / sum2
    # sum4 = log(x) - log(x) =  0
    sum5 = x ** 2 - 71 * x + 98
    sum6 = sin(x) + x ** 4 - 84
    sum7 = sum5 / sum6
    sum7 = sqrt(abs(sum7))
    sum0 = sum3 - sum7
    print_finish_num(sum0)


def practice2():
    x = float(input())
    if x < -27:
        sum0 = 32*x**4 + 47*x**6 + 92
    else:
        if -27 <= x < 40:
            sum0 = 79*x**6 + x + 6
        else:
            if x >= 40:
                sum0 = 86*x**8 - 64*x + 75
    print_finish_num(sum0)


def practice3():
    sum1 = 0
    sum2 = 0
    n = int(input())
    m = int(input())
    for i in range(1, n):
        for j in range(1, m):
            sum1 += i**5 - 47*i
            sum2 += i**6 + j**2 + 16
    sum0 = sum1 + sum2
    print_finish_num(sum0)


def practice4():
    n = int(input())
    sum0 = recursion4(n)
    print_finish_num(sum0)


def recursion4(x):
    if x == 0:
        x0 = 4
    elif x == 1:
        x0 = 3
    else:
        x0 = tan(recursion4(x - 1)) - cos(recursion4(x - 1))
    return x0


if __name__ == '__main__':
    # practice1()
    # practice2()
    # practice3()
    practice4()
