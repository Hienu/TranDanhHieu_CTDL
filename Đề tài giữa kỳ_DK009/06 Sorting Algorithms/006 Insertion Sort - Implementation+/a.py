# Hàm thực hiện thuật toán sắp xếp chèn
def insertion_sort(arr):
    n = len(arr)
    
    # Lặp qua từng phần tử trong mảng
    for i in range(1, n):
        key = arr[i]  # Phần tử cần chèn
        position = i
        
        # Di chuyển các phần tử lớn hơn key về phải
        while position > 0 and arr[position - 1] > key:
            arr[position] = arr[position - 1]
            position = position - 1
        
        # Chèn key vào đúng vị trí
        arr[position] = key
