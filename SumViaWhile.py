from typing import List

my_list = [7, 5, 4, 4, 2, 1, -5, -10, -15]
i = 0
suma = 0
while my_list[i] > 0:
    suma += my_list[i]
    i += 1

print(suma)

my_list2 = [7, 5, 4, 4, 2, 1]

i2 = 0
suma2 = 0
l = len(my_list2)
while i2 < l and my_list2[i2] > 0:
    suma2 += my_list2[i2]
    i2 += 1

print(suma2)
print(l)

suma = 0
l = len(my_list)
i = l-1

while i > 0 and my_list[i] < 0:
    suma += my_list[i]
    i-= 1

print(suma)





