def delete_max(heap):
    e = heap[1]  # Lấy giá trị ở gốc (là phần tử lớn nhất)
    heap[1] = heap[len(heap) - 1]  # Thay thế gốc bằng phần tử cuối cùng của heap
    heap.pop()  # Xóa phần tử cuối cùng của heap
    c_size = len(heap) - 1  # Cập nhật kích thước của heap
    i, j = 1, 2  # Thiết lập biến i và j

    # Down heap bubbling
    while j <= c_size:
        if j < c_size and heap[j] < heap[j + 1]:
            j += 1  # Chọn phần tử lớn hơn giữa hai con
        if heap[i] < heap[j]:
            heap[i], heap[j] = heap[j], heap[i]  # Hoán đổi phần tử với con lớn hơn
            i = j
            j *= 2
        else:
            break

    return e

heap = [None, 20, 15, 10, 5, 12, 8]
deleted_element = delete_max(heap)
print(f"Deleted Element: {deleted_element}")
print(f"Updated Heap: {heap}")
