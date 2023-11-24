# Ví dụ: In ra tất cả các số chẵn trong danh sách và sử dụng continue để bỏ qua số lẻ
numbers = [10, 54, 2, 61, 15]

print("Các số chẵn trong danh sách:")
for num in numbers:
    if num % 2 != 0:
        continue
    print(num)
