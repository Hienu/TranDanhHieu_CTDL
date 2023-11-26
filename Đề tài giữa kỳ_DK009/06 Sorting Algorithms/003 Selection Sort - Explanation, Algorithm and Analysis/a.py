# Ví dụ về sắp xếp chọn
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Áp dụng sắp xếp chọn cho một mảng
arr = [6, 3, 8, 2, 9, 1]
selection_sort(arr)
print("Mảng đã sắp xếp chọn:", arr)

# Ví dụ về sắp xếp chọn không ổn định
unstable_arr = [5, 2, 3, 5, 8, 6]
selection_sort(unstable_arr)
print("Sắp xếp không ổn định:", unstable_arr)

# Ví dụ về thời gian phức tạp của sắp xếp chọn
# (Số so sánh được thực hiện trong từng vòng lặp)
n = 6
comparisons = n * (n - 1) // 2
print("Số so sánh trong sắp xếp chọn:", comparisons)

# Kiểm tra tính ổn định của sắp xếp chọn
arr_with_duplicates = [(5, 'yellow'), (2, 'green'), (3, 'blue'), (5, 'white'), (8, 'red'), (6, 'black')]
selection_sort(arr_with_duplicates)
print("Sắp xếp không ổn định với phần tử trùng lặp:", arr_with_duplicates)

