# So sánh hiệu suất giữa các thuật toán với các thứ tự tăng khác nhau.

def constant_algorithm(arr):
    return arr[0]  # O(1)

def logarithmic_algorithm(arr):
    n = len(arr)
    return arr[n // 2]  # O(log N)

def quadratic_algorithm(arr):
    result = 0
    for i in arr:
        for j in arr:
            result += i * j
    return result  # O(N^2)
