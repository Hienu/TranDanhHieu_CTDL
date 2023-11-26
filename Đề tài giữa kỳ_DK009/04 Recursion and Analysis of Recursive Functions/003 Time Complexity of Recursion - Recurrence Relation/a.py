def calculate(n):
    if n == 0:
        return 0
    else:
        return calculate(n - 1) + n

# Test hàm với giá trị đầu vào n = 4
result = calculate(4)
print(f"The result is: {result}")
