# Сount the amount of elements in a list
my_text = "З Днем народження Днем достатку благополуччя миру любові успіхів народження достатку З Днем"
my_list = my_text.split()
print(my_list)
amount = len(my_list)
print(amount)
my_dict = {}
for element in my_list:
    if element in my_dict:
        my_dict[element] = my_dict[element] + 1
    else:
        my_dict[element] = 1

print(my_dict)

# 2 method
my_dict2 = {}
for element in my_list:
    if element in my_dict2:
        my_dict2[element] = my_dict2.get(element, 0) + 1
    else:
        my_dict2[element] = 1

print(my_dict2)
