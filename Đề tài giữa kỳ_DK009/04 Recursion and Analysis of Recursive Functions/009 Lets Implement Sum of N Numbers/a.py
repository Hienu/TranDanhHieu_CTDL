def sum_rec(n):
    if n == 0:
        return 0
    else:
        return sum_rec(n - 1) + n
num = input("Nhập số: ")
n = int(num)
print(sum_rec(n))
