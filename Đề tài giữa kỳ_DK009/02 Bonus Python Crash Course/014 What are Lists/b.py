my_list = [1, 2, 3, 'four', 5.0]
# Thao tác với danh sách
new_list = my_list + [6, 7]
my_list.insert(2, 'new_element')
my_list.append('last_element')
my_list.extend([8, 9, 10])

#print(new_list)
#print(my_list)

# Cập nhật và xóa phần tử
my_list[1] = 'updated_element'
del my_list[4]

#print(my_list)
# Slicing và sao chép danh sách
subset = my_list[1:4]
copy_list = my_list[:]

#print(subset)
#print(copy_list)
# Chuyển đổi chuỗi thành danh sách
my_string = "Hello World"
string_list = my_string.split()

#print(string_list)

