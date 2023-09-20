def zai_thua(n):
    if n == 0:
        return 1
    else:
        return n * zai_thua(n - 1)

# Nhập số từ bàn phím
try:
    num = int(input("Nhập một số nguyên không âm: "))
    if num < 0:
        print("Số bạn nhập phải là số nguyên không âm.")
    else:
        result = zai_thua(num)
        print(f"{num}! = {result}")
except ValueError:
    print("Số bạn nhập không hợp lệ. Vui lòng nhập một số nguyên không âm.")
