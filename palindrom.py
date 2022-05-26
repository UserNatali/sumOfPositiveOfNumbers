s1 = "bogogob"


def palindrom(s):
    list1 = []
    list1[:] = s[0:len(s)]
    print(list1)
    i = len(list1) - 1
    list2 = []
    while i >= 0:
        list2.append(list1[i])
        i += -1

    print(list2)
    l = len(list1) - 1
    for h in range(0, l):
        if list1[h] != list2[h]:
            return False

    return True


bool = palindrom(s1)
print(bool)
