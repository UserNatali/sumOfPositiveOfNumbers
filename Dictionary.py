# Turn the list into a dictionary
list = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourh", -50]
def dictionary(list):
    dict = {}
    currentKey = ""
    for element in list:
        if type(element) == str:
            currentKey = element
            dict[currentKey] = []
        else:
            arr = dict[currentKey]
            arr.append(element)

    return dict

print(dictionary(list))

