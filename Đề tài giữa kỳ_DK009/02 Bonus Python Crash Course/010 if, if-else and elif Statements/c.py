# Kiểm tra số nhập từ người dùng và in ra kết quả
user_input = float(input("Nhập một số: "))

if user_input > 0:
    print("Số dương.")
elif user_input == 0:
    print("Số không.")
else:
    print("Số âm.")
