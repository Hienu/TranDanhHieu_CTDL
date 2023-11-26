# Hàm băm sử dụng phép chia lấy dư
def modulo_hash_function(key, table_size):
    return key % table_size

# Sử dụng hàm băm để lưu trữ dữ liệu trong bảng hash
table_size = 10
data = [54, 78, 63, 92, 45, 86]

hash_table = [None] * table_size

for element in data:
    hash_value = modulo_hash_function(element, table_size)
    hash_table[hash_value] = element

print("Hash Table with Modulo Hashing:", hash_table)
