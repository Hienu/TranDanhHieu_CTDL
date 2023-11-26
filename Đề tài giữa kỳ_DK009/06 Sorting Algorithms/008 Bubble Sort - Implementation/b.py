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
