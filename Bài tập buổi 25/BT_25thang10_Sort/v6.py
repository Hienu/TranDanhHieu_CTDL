def insertionsort(A):
    n=len(A)
    for i in range(1,n):
        cvalue = A[i]
        position = i
        while position >0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position = position - 1
        A[position] = cvalue


A=[1,7,3,10,2003,2003]
print('Original Array:', A)

insertionsort(A)   
print('Sorted Array:', A)
