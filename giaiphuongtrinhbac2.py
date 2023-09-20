import math

a = float(input("Nhập vào hệ số a khác 0: "))
b = float(input("Nhập vào hệ số b: "))
c = float(input("Nhập vào hệ số c: "))

delta=b**2-4*a*c
print(f"Delta có giá trị là {delta}")

if delta<0:
    print("Phương trình vô nghiệm!")
else:
    if delta>0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print(f"Phương trình đã cho có hai nghiệm phân biệt là: {x1:.0f} và {x2:.0f}")
    else:
        x0=(-b)/(2*a)
        print(f"Phương trình đã cho có nghiệm kép là: {x0}")