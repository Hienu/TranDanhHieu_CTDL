def calculate_time_complexity(n):
    if n == 0:
        return 1  # Đơn vị thời gian cho trường hợp cơ bản
    else:
        return calculate_time_complexity(n - 1) + 3  # Giả sử có 3 đơn vị thời gian cho mỗi lần đệ quy

# Tính độ phức tạp thời gian cho n = 4
time_complexity_result = calculate_time_complexity(4)
print(f"Time complexity for n = 4 is: {time_complexity_result}")
