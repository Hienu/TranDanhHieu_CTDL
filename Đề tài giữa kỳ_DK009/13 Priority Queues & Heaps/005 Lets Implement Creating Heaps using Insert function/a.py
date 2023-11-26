class Heap:
    def __init__(self):
        self._max_size = 10
        self._data = [-1] * self._max_size
        self._size = 0

    def is_empty(self):
        return len(self._data) == 0

    def insert(self, e):
        if self._size == self._max_size:
            print("No space")
            return
        self._size += 1
        i = self._size
        while i > 1 and e > self._data[i // 2]:
            self._data[i] = self._data[i // 2]
            i //= 2
        self._data[i] = e

    def max_element(self):
        if self.is_empty():
            print("Heap is empty")
            return
        return self._data[1]

# Sử dụng lớp Heap để chèn phần tử vào heap và in ra các phần tử của heap.
heap = Heap()
heap.insert(25)
heap.insert(20)
heap.insert(2)
heap.insert(14)
heap.insert(10)
print(heap._data)  # Kết quả in ra các phần tử của heap.
