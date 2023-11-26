def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return factorial_rec(n - 1) * n
num = int(input("Enter number: "))
result = factorial_rec(num)
print(f"The factorial of {num} is: {result}")

# Ví dụ
num1 = 4
result1 = factorial_rec(num1)
print(f"The factorial of {num1} is: {result1}")

num2 = 5
result2 = factorial_rec(num2)
print(f"The factorial of {num2} is: {result2}")

