# Kết luận về độ phức tạp thời gian
def conclusion(n):
    if n == 0:
        return 0
    else:
        return conclusion(n-1) + n

# Độ phức tạp thời gian là O(n^2)
n = 5
result = conclusion(n)
print(f"Độ phức tạp thời gian O(n^2) cho n = {n}")
