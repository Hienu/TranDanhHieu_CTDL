def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        position = i
        for j in range(i + 1, n):
            if a[j] < a[position]:
                position = j
        temp = a[i]
        a[i] = a[position]
        a[position] = temp

# Tạo mảng
a = [3, 5, 8, 9, 6]

# In ra mảng trước khi sắp xếp
print("Original array:", a)

# Gọi hàm sắp xếp chọn
selection_sort(a)

# In ra mảng sau khi sắp xếp
print("Sorted array:", a)

