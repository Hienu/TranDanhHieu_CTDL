def countsort(A):
    n = len(A)
    maxsize = max(A)
    carray = [0] * (maxsize+1)
    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1
    i = 0
    j = 0
    while i < maxsize + 1:
        if carray[i] > 0:
            A[j] = i
            j = j + 1
            carray[i] = carray[i] - 1
        else:
            i = i + 1

A = [1, 7, 3, 10, 2003, 2003]
print('Original Array:', A)

countsort(A)
print('Sorted Array:', A)