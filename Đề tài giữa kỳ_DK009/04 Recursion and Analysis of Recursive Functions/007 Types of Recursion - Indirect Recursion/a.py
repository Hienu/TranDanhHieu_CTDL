def calculate_A():
    print("Calculate A")
    calculate_B()

def calculate_B():
    print("Calculate B")
    calculate_A()

# Gọi hàm ban đầu
calculate_A()
