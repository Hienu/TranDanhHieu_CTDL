# Ví dụ: In ra tất cả các số lẻ trong danh sách và sử dụng continue để bỏ qua số chẵn
numbers = [10, 54, 2, 61, 15]

print("Các số lẻ trong danh sách:")
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
