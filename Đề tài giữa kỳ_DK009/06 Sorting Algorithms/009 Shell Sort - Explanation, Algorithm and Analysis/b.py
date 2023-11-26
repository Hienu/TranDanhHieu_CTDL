def shellsort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            value = arr[i]
            j = i
            while j >= gap and arr[j - gap] > value:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = value
        gap //= 2
