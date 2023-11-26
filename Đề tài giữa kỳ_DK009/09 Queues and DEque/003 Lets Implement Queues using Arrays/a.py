class QueueArray:
    def __init__(self):
        self._data = []  # Danh sách để lưu trữ các phần tử của hàng đợi

    def length(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, element):
        self._data.append(element)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self._data[0]
    

    def length(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, element):
        self._data.append(element)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self._data[0]


# Tạo đối tượng hàng đợi
queue = QueueArray()

# Thêm phần tử vào hàng đợi
queue.enqueue(5)
queue.enqueue(3)

# Hiển thị các phần tử trong hàng đợi
print(queue._data)

# Hiển thị độ dài của hàng đợi
print("Length:", queue.length())

# Thêm thêm phần tử vào hàng đợi
queue.enqueue(7)
queue.enqueue(12)

# Hiển thị các phần tử trong hàng đợi
print(queue._data)

# Loại bỏ một phần tử khỏi hàng đợi
removed_element = queue.dequeue()
print("Removed Element:", removed_element)

# Hiển thị lại các phần tử trong hàng đợi
print(queue._data)

# Lấy phần tử ở đầu hàng đợi
front_element = queue.first()
print("Front Element:", front_element)
