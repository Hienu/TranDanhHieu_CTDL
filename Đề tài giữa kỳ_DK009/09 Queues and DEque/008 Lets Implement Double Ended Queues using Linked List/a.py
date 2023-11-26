
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class LinkedList:
    def __init__(self):
        self.front = None  # thay vì self.head
        self.rear = None   # thay vì self.tail
        self.size = 0


    def display(self):
        current = self.front  # thay vì self.head
        while current:
            print(current.element, end=" ")
            current = current.next
        print("\n")


    def add_first(self, element):
        new_node = Node(element)
        new_node.next = self.front  # thay vì self.head
        self.front = new_node


    def remove_first(self):
        if self.is_empty():
            print("Linked list is empty")
            return None
        else:
            removed_element = self.front.element  # thay vì self.head
            self.front = self.front.next
            self.size -= 1
            return removed_element

