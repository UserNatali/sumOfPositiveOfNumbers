# Array mirroring
array = [[1, 2, 3, 11], [4, 5, 6, 12], [7, 8, 9, 13], [21, 22, 23, 24]]


def list_array(array):
    for element in array:
        for el in element:
            print(el, end=" ")
        print()


list_array(array)


def reverse_array(array):
    result_array = []
    for nested_array in array:
        result_nested_array = []
        for index in range(len(nested_array) - 1, -1, -1):
            element = nested_array[index]
            result_nested_array.append(element)
        result_array.append(result_nested_array)
    return result_array


list_array(reverse_array(array))


def reverse_array_2(array):
    for str in array:
        for i in range(len(array) // 2):
            swap(str, i, len(array) - 1 - i)


def swap(array, i, j):
    temt = array[i]
    array[i] = array[j]
    array[j] = temt


reverse_array_2(array)
list_array(array)
