import random

l1 = sorted([random.randrange(5) for i in range(10)])
l2 = sorted([random.randrange(5) for i in range(10)])

# l1 = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
# l2 = [0, 0, 0, 1, 2, 2, 2, 4, 4, 4]

print(l1)
print(l2)
res = []
i, j = 0, 0
while i != len(l1) and j != len(l2):
    if l1[i] == l2[j]:
        print(l1[i], end=', ')
        i += 1
        j += 1
    elif l1[i] > l2[j]:
        j += 1
    else:
        i += 1
