import random

lst = [1, 2, 3, 5, 6, 7, 8, 9]
el = int(input('> '))
i = 0
j = len(lst)

while True:

    median = (i+j)//2
    if lst[median] < el:
        i += (median//2)
    elif lst[median] > el:
        j //= 2
    else:
        print(el)
        break
    if median > len(lst) or i > j or median <= 0:
        print(False)
        break
