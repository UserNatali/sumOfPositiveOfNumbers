set = {7, 5, 10, 11, 23}
list = [11, 5, 23, 7]
print(17 in set)
set.add(15)
set.add(7)
print(set)


def function(set, list):
    if len(list) > len(set):
        return False

    for element in list:
        if element not in set:
            return False
    return True


print(function(set, list))
