# Ví dụ: Tìm kiếm số trong danh sách và sử dụng break để kết thúc ngay lập tức nếu tìm thấy
numbers = [10, 54, 2, 61, 15]

search_key = int(input("Nhập số cần tìm: "))

for num in numbers:
    if num == search_key:
        print("Số đã được tìm thấy trong danh sách.")
        break
else:
    print("Số không có trong danh sách.")
54