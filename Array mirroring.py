# Array mirroring
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def list_array(l):
    for element in l:
        for el in element:
            print(el, end=" ")
        print()


list_array(array)
r = len(array)


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
