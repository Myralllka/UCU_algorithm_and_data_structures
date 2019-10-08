import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 +
                         (self.y - other.y) ** 2)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __hash__(self):
        return hash(self.x)


def solution(a):
    ax = sorted(a, key=lambda x: x.x)
    ay = sorted(a, key=lambda x: x.y)
    p1, p2, minimum_value = closest_pair(ax, ay)
    return minimum_value, p1, p2


def check_three_dots(subarr_x):
    p1 = subarr_x[0]
    p2 = subarr_x[1]
    min_value = p1.distance_to(p2)
    length = len(subarr_x)
    if length == 2:
        return p1, p2, min_value
    for i in range(length - 1):
        for j in range(i + 1, length):
            if i and j != 1:
                d = subarr_x[i].distance_to(subarr_x[j])
                if d < min_value:
                    min_value = d
                    p1, p2 = subarr_x[i], subarr_x[j]
    return p1, p2, min_value


def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)
    mx_x = p_x[ln_x // 2].x
    s_y = [x for x in p_y if mx_x - delta <= x.x <= mx_x + delta]
    best = delta
    ln_y = len(s_y)
    for i in range(ln_y - 1):
        for j in range(i + 1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = p.distance_to(q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best


def closest_pair(px, py):
    length = len(px)
    if length <= 3:
        return check_three_dots(px)
    middle = length // 2
    qx = px[middle:]
    rx = px[:middle]
    setq = set(qx)
    qy = []
    ry = []
    for x in py:
        if x in setq:
            qy.append(x)
        else:
            ry.append(x)

    (p1, q1, min_val_1) = closest_pair(qx, qy)
    (p2, q2, min_val_2) = closest_pair(rx, ry)
    if min_val_1 <= min_val_2:
        d = min_val_1
        mn = (p1, q1)
    else:
        d = min_val_2
        mn = (p2, q2)

    (p3, q3, min_val_3) = closest_split_pair(px, py, d, mn)
    if d <= min_val_3:
        return mn[0], mn[1], d
    else:
        return p3, q3, min_val_3


def input(filename):
    result = []
    with open(filename, 'r') as ff:
        for each in ff.readlines():
            (x, y) = list(map(int, each.split()))
            result.append(Point(x, y))
    # print(result)
    return result


print(solution(input('input_100.txt')))
