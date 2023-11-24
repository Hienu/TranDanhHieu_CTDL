# Sắp xếp và thống kê danh sách
num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
num_list.sort()
num_list.reverse()

length = len(num_list)
total = sum(num_list)
minimum = min(num_list)
maximum = max(num_list)

print(num_list)
print(length, total, minimum, maximum)

# Toán tử thành viên
print(3 in num_list)    # Output: True
print(7 not in num_list)  # Output: True
