# Chương trình Python thực hiện Bubble Sort
def bubblesort(a):
    n = len(a)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if a[i] > a[i + 1]:
                # Hoán đổi các phần tử nếu cần
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp

# Sử dụng chương trình
my_list = [3, 5, 8, 9, 6, 2]
print("Dãy số ban đầu:", my_list)
bubblesort(my_list)
print("Dãy số sau khi sắp xếp:", my_list)
