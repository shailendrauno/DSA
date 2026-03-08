def bubbleShort(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-1-i):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

a = [23,34,43,2,13,1,76]
bubbleShort(a)
print(a)