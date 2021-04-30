def f13(n, m):
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum1 += i**5 - 47*i
            sum2 += i**6 + j**2 + 16
    sum0 = sum1 + sum2
    return sum0
