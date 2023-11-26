def calculate_rec(n):
    if n > 0:
        k = n ** 2
        print(k)
        calculate_rec(n - 1)
calculate_rec(4)
