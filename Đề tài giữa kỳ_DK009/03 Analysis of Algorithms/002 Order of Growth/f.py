# Ví dụ về thuật toán có thời gian chạy bậc hai và bậc ba.

def quadratic_time_algorithm(arr):
    result = 0
    for i in arr:
        for j in arr:
            result += i * j
    return result  # O(N^2)

def cubic_time_algorithm(arr):
    result = 0
    for i in arr:
        for j in arr:
            for k in arr:
                result += i * j * k
    return result  # O(N^3)
