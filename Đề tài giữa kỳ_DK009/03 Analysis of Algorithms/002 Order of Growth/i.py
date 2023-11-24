# Ví dụ về thuật toán quan trọng sử dụng chia để trị.

def linear_algorithm(arr):
    for num in arr:
        print(num)

def logarithmic_n_log_n_algorithm(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        # Gọi đệ quy cho từng nửa
        logarithmic_n_log_n_algorithm(left_half)
        logarithmic_n_log_n_algorithm(right_half)
