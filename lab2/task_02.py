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

    def perimeter(self, other1, other2):
        if self == other2 or self == other1 or other2 == other1:
            return 2 ** 18
        a = self.distance_to(other1)
        b = self.distance_to(other2)
        c = other1.distance_to(other2)

        if a + b > c or a + c > b or b + c > a:
            return a + b + c
        else:
            return 2 ** 18

    def to_lst(self):
        return [self.x, self.y]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "{} {}".format(self.x, self.y)

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def closest_triple(px, py):
    length = len(px)
    if length <= 5:
        return check_five_dots(px)
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
    (p1, q1, r1, min_val_1) = closest_triple(qx, qy)
    (p2, q2, r2, min_val_2) = closest_triple(rx, ry)
    if min_val_1 <= min_val_2:
        d = min_val_1
        mn = (p1, q1, r1)
    else:
        d = min_val_2
        mn = (p2, q2, r2)
    (p3, q3, r3, min_val_3) = closest_split_triple(px, py, d, mn)
    if d <= min_val_3:
        return mn[0], mn[1], mn[2], d
    return p3, q3, r3, min_val_3


def check_five_dots(subarr_x):
    p1, p2, p3 = subarr_x[0], subarr_x[1], subarr_x[2]
    min_val = p1.perimeter(p2, p3)
    length = len(subarr_x)
    if length == 3:
        return p1, p2, p3, min_val
    for i in range(length - 2):
        for j in range(i + 1, length):
            if i and j != 1:
                d = subarr_x[i].perimeter(subarr_x[i + 1], subarr_x[i + 2])
                if d < min_val:
                    min_val = d
                    p1, p2, p3 = subarr_x[i], subarr_x[i + 1], subarr_x[i + 2]
    return p1, p2, p3, min_val


def closest_split_triple(p_x, p_y, delta, best_triple):
    len_x = len(p_x)
    max_x = p_x[len_x // 2].x
    list_y = [x for x in p_y if max_x - delta <= x.x <= max_x + delta]
    best = delta
    len_y = len(list_y)
    for i in range(len_y - 1):
        for j in range(i + 1, min(i + 7, len_y)):
            for k in range(j + 1, min(j + 7, len_y)):
                p, q, r = list_y[i], list_y[j], list_y[k]
                perimeter = p.perimeter(q, r)
                if perimeter < best:
                    best_triple = p, q, r
                    best = perimeter
    return best_triple[0], best_triple[1], best_triple[2], best


def closest_split_pair(p_x, p_y, delta, best_pair):
    len_x = len(p_x)
    max_x = p_x[len_x // 2].x
    list_y = [x for x in p_y if max_x - delta <= x.x <= max_x + delta]
    best = delta
    len_y = len(list_y)
    for i in range(len_y - 1):
        for j in range(i + 1, min(i + 7, len_y)):
            p, q = list_y[i], list_y[j]
            distance = p.distance_to(q)
            if distance < best:
                best_pair = p, q
                best = distance
    return best_pair[0], best_pair[1], best


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


def find_closest_pair(px, py):
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
    (p1, q1, min_val_1) = find_closest_pair(qx, qy)
    (p2, q2, min_val_2) = find_closest_pair(rx, ry)
    if min_val_1 <= min_val_2:
        d = min_val_1
        mn = (p1, q1)
    else:
        d = min_val_2
        mn = (p2, q2)
    (p3, q3, min_val_3) = closest_split_pair(px, py, d, mn)
    if d <= min_val_3:
        return mn[0], mn[1], d
    return p3, q3, min_val_3


def minimal_perimeter(in_lst):
    a = []
    i = 0
    ll = len(in_lst)
    while i < ll:
        a.append(Point(in_lst[i][0], in_lst[i][1]))
        i += 1
    ax = sorted(a, key=lambda x: x.x)
    ay = sorted(a, key=lambda x: x.y)
    p1, p2, p3, minimum_value = closest_triple(ax, ay)
    return minimum_value, (p1.to_lst(), p2.to_lst(), p3.to_lst())


def closest_pair(in_lst):
    a = []
    i = 0
    ll = len(in_lst)
    while i < ll:
        a.append(Point(in_lst[i][0], in_lst[i][1]))
        i += 1
    ax = sorted(a, key=lambda x: x.x)
    ay = sorted(a, key=lambda x: x.y)
    p1, p2, minimum_value = find_closest_pair(ax, ay)
    return minimum_value, (p1.to_lst, p2.to_lst)


def input(filename):
    result = []
    ff = open(filename, 'r')
    n = ff.readline()
    for each in ff.readlines():
        (x, y) = list(map(int, each.split()))
        result.append(Point(x, y))
    ff.close()
    return result


if __name__ == "__main__":
    # print(closest_pair(input('input_100.txt')))
    # print(minimal_perimeter(input('input_100.txt')))
    print(closest_pair([82, 66, 33, 62, 98, 19, 41, 25, 92, 94, 17, 29, 78, 30, 25, 92,19, 82, 42, 31]))
    print(minimal_perimeter([82, 66, 33, 62, 98, 19, 41, 25, 92, 94, 17, 29, 78, 30, 25, 92,19, 82, 42, 31]))
