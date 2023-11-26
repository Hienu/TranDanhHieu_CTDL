# Tạo đối tượng DEQ
d = DeckArray()

# Thêm phần tử từ đầu và cuối DEQ
d.add_first(5)
d.add_first(3)
d.add_last(7)
d.add_last(12)

# In ra các phần tử và độ dài DEQ
print("Elements of DEQ:", d._data)
print("Length of DEQ:", d.length())

# Loại bỏ phần tử từ đầu và cuối DEQ
removed_first = d.remove_first()
removed_last = d.remove_last()

# In ra các phần tử và độ dài DEQ sau khi loại bỏ
print("Removed First:", removed_first)
print("Removed Last:", removed_last)
print("Updated Elements of DEQ:", d._data)
print("Updated Length of DEQ:", d.length())

# Lấy phần tử đầu và cuối DEQ
print("First Element:", d.first())
print("Last Element:", d.last())
