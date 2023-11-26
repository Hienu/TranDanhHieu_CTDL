def power_of_two(n):
    # Điều kiện cơ bản
    if n == 0:
        return 1
    else:
        # Gọi chính nó
        result = 2 * power_of_two(n - 1)
        print(f"2^{n} = {result}")
        return result

# Gọi hàm đệ quy
power_of_two(3)
