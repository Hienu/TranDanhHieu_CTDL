my_list = [1, 2, 3, 'four', 5.0]
# Thao tác với danh sách
new_list = my_list + [6, 7]
my_list.insert(2, 'new_element')
my_list.append('last_element')
my_list.extend([8, 9, 10])

print(new_list)
print(my_list)
