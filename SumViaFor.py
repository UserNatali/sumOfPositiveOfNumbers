my_list = [7, 5, 4, 4, 2, 1, -5, -10, -15]
sum = 0
l = len(my_list)
x = range(l - 1, -1, -1)
for index in x:
    if my_list[index] < 0:
        sum += my_list[index]
    else:
        break
print(sum)
