
list = [numb *2 for numb in range(10, 1, -1) if numb % 2 == 0]
print(list)

list_str = ["hello", "hey", "goodbye", "quitar", "piano"]
list_str_new = [word + "." for word in list_str if len(word) > 5]
print(list_str_new)