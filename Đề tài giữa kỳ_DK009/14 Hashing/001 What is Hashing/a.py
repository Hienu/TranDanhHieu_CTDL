# Ví dụ đơn giản về hàm băm
def simple_hash_function(key, table_size):
    return key % table_size

# Sử dụng hàm băm để ánh xạ các phần tử vào vị trí trong bảng hash
table_size = 10
data = [3, 5, 8, 9, 6, 2]

for element in data:
    hash_value = simple_hash_function(element, table_size)
    print(f"Element {element} is mapped to index {hash_value} in the hash table.")

# Tìm kiếm tuyến tính
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Sử dụng hashing để tìm kiếm
def hash_search(data, target, hash_function, table_size):
    hash_value = hash_function(target, table_size)
    if data[hash_value] == target:
        return hash_value
    else:
        return -1

# Áp dụng tìm kiếm tuyến tính và tìm kiếm bằng hashing cho dữ liệu
data = [3, 5, 8, 9, 6, 2]
target = 8
linear_search_result = linear_search(data, target)
hash_search_result = hash_search(data, target, simple_hash_function, len(data))

print(f"Linear Search Result: Element {target} found at index {linear_search_result}.")
print(f"Hash Search Result: Element {target} found at index {hash_search_result}.")

# Hàm băm 1-1 (ideal hashing)
def ideal_hash_function(key):
    return key

# Sử dụng bảng hash với hàm băm 1-1
hash_table = [None] * 13  # Khởi tạo bảng hash với kích thước 13
data = [3, 5, 8, 9, 6, 2]

for element in data:
    hash_value = ideal_hash_function(element)
    hash_table[hash_value] = element

print("Hash Table with Ideal Hashing:", hash_table)
