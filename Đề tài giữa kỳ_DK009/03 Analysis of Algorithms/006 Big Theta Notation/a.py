# Ví dụ với 5N + 4 là Theta(N)
# Chọn C1 = 1, C2 = 6, N0 = 4
C1 = 1
C2 = 6
N0 = 4

# Định nghĩa biến N
N = 10
# Kiểm tra điều kiện
if C1 * N >= 5 * N + 4 >= C2 * N:
    print("5N + 4 is Theta(N)")
