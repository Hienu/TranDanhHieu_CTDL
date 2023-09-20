def zaithua(n):
    if n ==0:
        return 1
    else:
        return n * zaithua(n-1)

while True:
    a = int(input("Nhập vào 1 số a không âm: "))
    
    if a>=0:
        ketqua = zaithua(a)
        print(f"Kết quả thu được là: {a}! = {ketqua}")
        break
    else:
        print("Số bạn nhập không hợp lệ, xin vui lòng nhập lại 1 số nguyên không âm: ")

