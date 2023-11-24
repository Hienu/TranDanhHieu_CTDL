t = (10, 'Hello', 2.85)
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
new_tuple = t1 + t2
#print(new_tuple)  # Kết quả: (1, 2, 3, 'a', 'b', 'c')

subset = t[0:2]  # Trích xuất các phần tử từ 0 đến 1
#print(subset)  # Kết quả: (10, 'Hello')

length = len(t)
#print(length)  # Kết quả: 3

is_present = 54 in t
print(is_present)  # Kết quả: False