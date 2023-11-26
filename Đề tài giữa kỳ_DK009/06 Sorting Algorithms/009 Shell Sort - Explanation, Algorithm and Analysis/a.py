def shellsort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            value = arr[i]
            j = i
            while j >= gap and arr[j - gap] > value:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = value
        gap //= 2

# Sử dụng chương trình
my_array = [6, 3, 9, 5, 2]
print("Mảng ban đầu:", my_array)
shellsort(my_array)
print("Mảng sau khi sắp xếp:", my_array)
