def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return sum_of_natural_numbers(n - 1) + n

result = sum_of_natural_numbers(5)
print(result)  # Output: 15
