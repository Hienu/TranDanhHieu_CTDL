def fact_of_N(n):
    if n == 0:
        return 1
    else:
        return fact_of_N(n - 1) * n
