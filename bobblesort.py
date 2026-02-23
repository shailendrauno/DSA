
def bubblesortDes (a):
    n = len(a)

    for i in range(n):
        for j in range (0, n-1-i):
            if(a[j+1] > a[j]):
                a[j+1], a[j] = a[j], a[j+1]
a = [1,2,3,4,5,6,7,8,9]
bubblesortDes(a)
print(a)


def bubblesortAss(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-1-i):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

a = [12,11,8,5,4,32,1]
bubblesortAss(a)
print(a)