a = [i for i in range(10)]
b = [i for i in range(0, 20, 3)]
x, y = 0, 0
result = []
while x <= len(a) - 1 and y <= len(b) - 1:
    if a[x] >= b[y]:
        result.append(b[y])
        y += 1
    else:
        result.append(a[x])
        x += 1
else:
    if x >= len(a):
        result.extend(b[y:])
    else:
        result.extend(a[x:])

print(result)
