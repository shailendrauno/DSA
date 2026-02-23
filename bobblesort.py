def bubblesort(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-1-i):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

a = [12,11,8,5,4,32,1]
bubblesort(a)
print(a)


def bubblesort (a):
    n = len(a)

    for i in range(n):
        for j in range (0, j-1-i):
            if(a[j+1] > a[j]):
                a[j+1], a[j] = a[j], a[j+1]
