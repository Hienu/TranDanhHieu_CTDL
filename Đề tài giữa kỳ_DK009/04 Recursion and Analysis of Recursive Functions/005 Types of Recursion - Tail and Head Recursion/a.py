def calculate_tail_recursive(n, result=0):
    # Base case
    if n == 0:
        return result
    # Tail recursive call
    return calculate_tail_recursive(n-1, result + n*n)

# Test with N = 4
result = calculate_tail_recursive(4)
print(result)
