# Sử dụng Chaining để lưu trữ dữ liệu trong bảng hash
hash_table = [None] * 10
data = [54, 78, 64, 92, 34, 86, 28]

def hash_function(key):
    return key % 10

for element in data:
    hash_value = hash_function(element)
    if hash_table[hash_value] is None:
        hash_table[hash_value] = [element]
    else:
        hash_table[hash_value].append(element)

print("Hash Table with Chaining:", hash_table)

# Lựa chọn hàm băm và kích thước bảng hash
def custom_hash_function(key, table_size):
    return key % table_size

# Ví dụ: Sử dụng hàm băm mới cho việc lưu trữ dữ liệu
new_hash_table = [None] * 15
for element in data:
    hash_value = custom_hash_function(element, 15)
    if new_hash_table[hash_value] is None:
        new_hash_table[hash_value] = [element]
    else:
        new_hash_table[hash_value].append(element)

print("New Hash Table with Custom Hashing:", new_hash_table)
