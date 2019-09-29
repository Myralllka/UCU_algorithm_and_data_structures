import random

lst = [1, 5, 10, 20, 30, 50, 60, 70, 80, 90]
el = int(input('> '))
i = 0
j = len(lst)

while True:
    median = int(bin(i+j)[2:-1], 2)
    if lst[median] < el:
        i += int(bin(median)[2:-1], 2)
    elif lst[median] > el:
        j = int(bin(j)[2:-1], 2)
    else:
        print(el)
        break
    if median > len(lst) or i > j or median <= 0:
        print(False)
        break
