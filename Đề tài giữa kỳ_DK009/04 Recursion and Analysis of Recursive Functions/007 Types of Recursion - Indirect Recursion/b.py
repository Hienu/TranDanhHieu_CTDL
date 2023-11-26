def calculate_A(count):
    if count > 0:
        print("Calculate A")
        calculate_B(count - 1)

def calculate_B(count):
    if count > 0:
        print("Calculate B")
        calculate_A(count - 1)

# Gọi hàm ban đầu với điều kiện cơ bản
calculate_A(3)
