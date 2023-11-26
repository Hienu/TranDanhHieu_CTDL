# Giải mối quan hệ đệ quy t(n) = t(n-1) + n
def solve_recursive_relation(n):
    if n == 0:
        return 0
    else:
        return solve_recursive_relation(n-1) + n

result = solve_recursive_relation(5)
print(f"The result is: {result}")
