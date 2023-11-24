# Ví dụ về thuật toán với thứ tự tăng hằng số và logarithmic.

def constant_time_algorithm(arr):
    return arr[0]  # O(1)

def logarithmic_time_algorithm(arr):
    n = len(arr)
    return arr[n // 2]  # O(log N)
