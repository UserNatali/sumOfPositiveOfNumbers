m1 = 3
n1 = 3

def array(m,n):
    arr = []
    for i in range(m):
        list = []
        for j in range(n):
            list.append(0)
        arr.append(list)

    return arr
print(array(3,3))




