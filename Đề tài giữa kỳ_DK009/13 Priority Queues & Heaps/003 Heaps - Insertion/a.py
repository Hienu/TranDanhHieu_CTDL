# Mã nguồn minh họa cho việc chèn phần tử vào heap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)  # Tạo một nút mới
        index = len(self.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                # Swap nếu phá vỡ thuộc tính liên quan
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

# Thực hiện chèn một số phần tử vào heap
max_heap = MaxHeap()
max_heap.insert(20)
max_heap.insert(14)
max_heap.insert(2)
max_heap.insert(15)
max_heap.insert(10)
max_heap.insert(21)

print(max_heap.heap)

# Mã nguồn minh họa cho up heap bubbling
# Sử dụng class MaxHeap từ ví dụ trước
# ...

# Gọi phương thức insert để thấy up heap bubbling trong hành động
max_heap.insert(25)
print(max_heap.heap)
