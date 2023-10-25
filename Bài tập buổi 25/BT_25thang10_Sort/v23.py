def radixsort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    bins = [[] for _ in range(10)]

    for i in range(digits):
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            bins[e].append(A[j])
        
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x][y]
                    k = k + 1
                bins[x] = []

A = [1, 7, 3, 10, 2003, 2003]
print('Original Array:', A)

radixsort(A)
print('Sorted Array:', A)
