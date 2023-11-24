# Ví dụ về thuật toán có thời gian chạy tuyến tính.

def linear_time_algorithm(arr):
    total = 0
    for num in arr:
        total += num
    return total  # O(N)
