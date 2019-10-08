a = [i for i in range(10)]
b = [i for i in range(20)]
c = [i for i in range(5)]

def m(l1,l2):
    x, y = 0, 0
    result = []
    while x <= len(l1) - 1 and y <= len(l2) - 1:
        if l1[x] >= l2[y]:
            result.append(l2[y])
            y += 1
        else:
            result.append(l1[x])
            x += 1
    else:
        if x >= len(l1):
            result.extend(l2[y:])
        else:
            result.extend(l1[x:])
    return result

print(m(a, m(b, c)))
