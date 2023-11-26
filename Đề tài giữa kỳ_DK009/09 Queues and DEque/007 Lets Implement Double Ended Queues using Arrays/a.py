class DeckArray:
    def __init__(self):
        self._data = []

    def length(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self, element):
        self._data.insert(0, element)

    def add_last(self, element):
        self._data.append(element)

    def remove_first(self):
        if self.is_empty():
            print("Deck is empty")
            return
        return self._data.pop(0)

    def remove_last(self):
        if self.is_empty():
            print("Deck is empty")
            return
        return self._data.pop()

    def first(self):
        if self.is_empty():
            print("Deck is empty")
            return
        return self._data[0]

    def last(self):
        if self.is_empty():
            print("Deck is empty")
            return
        return self._data[-1]

# Tạo đối tượng DEQ
d = DeckArray()

# Thêm phần tử từ đầu và cuối DEQ
d.add_first(5)
d.add_first(3)
d.add_last(7)
d.add_last(12)

# In ra các phần tử và độ dài DEQ
print("Elements of DEQ:", d._data)
print("Length of DEQ:", d.length())

# Loại bỏ phần tử từ đầu và cuối DEQ
removed_first = d.remove_first()
removed_last = d.remove_last()

# In ra các phần tử và độ dài DEQ sau khi loại bỏ
print("Removed First:", removed_first)
print("Removed Last:", removed_last)
print("Updated Elements of DEQ:", d._data)
print("Updated Length of DEQ:", d.length())

# Lấy phần tử đầu và cuối DEQ
print("First Element:", d.first())
print("Last Element:", d.last())
