def factorial_recursive(n):
    # Điều kiện cơ bản
    if n == 0 or n == 1:
        return 1
    else:
        # Gọi chính nó
        return n * factorial_recursive(n - 1)

# Gọi hàm đệ quy
result = factorial_recursive(5)
print(f"The factorial of 5 is: {result}")
