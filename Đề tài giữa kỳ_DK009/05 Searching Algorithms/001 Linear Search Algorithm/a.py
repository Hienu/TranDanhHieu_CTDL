# Mô tả quá trình tìm kiếm
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Ví dụ cụ thể
array_example = [84, 21, 47, 96, 15]
key_to_find = 21
result = linear_search(array_example, key_to_find)
print(f"The element {key_to_find} is at index {result} in the array.")

key_to_find = 100
result = linear_search(array_example, key_to_find)
print(f"The element {key_to_find} is at index {result} in the array.")
