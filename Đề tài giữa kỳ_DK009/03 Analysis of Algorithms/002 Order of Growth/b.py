# Ví dụ về cách loại bỏ hằng số khi xem xét thứ tự tăng.

def constant_time_algorithm(arr):
    return arr[0]  # O(1)

def linear_time_algorithm(arr):
    total = 0
    for num in arr:
        total += num
    return total  # O(N)

def quadratic_time_algorithm(arr):
    result = 0
    for i in arr:
        for j in arr:
            result += i * j
    return result  # O(N^2)
