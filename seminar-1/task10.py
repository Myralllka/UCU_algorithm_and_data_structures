import random

ll = [random.randrange(100) for i in range(10)]

print(ll)
def quick_sort(line):
    if len(line) <= 1:
        return line
    l_line, m_line, r_line = [], [random.choice(line)], []
    for n in line:
        if n < m_line[0]:
            l_line.append(n)
        elif n > m_line[0]:
            r_line.append(n)
    return quick_sort(l_line) + m_line + quick_sort(r_line)

ll = quick_sort(ll)
minn = ll[1]-ll[0]
n = ll[0]
m = ll[1]

for i in range(len(ll)-1):
    if (ll[i+1] - ll[i]) < minn:
        minn = ll[i+1] - ll[i]
        n = ll[i]
        m = ll[i+1]

print(ll)
print(n, m)