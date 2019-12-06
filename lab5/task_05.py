import json


def knapsack(items: list, total_weight):
    """

    :param total_weight:
    :param items: (value, weight)
    :return:
    """
    if len(items) >= 500:
        return 0, 0
    result_items = []
    size = (total_weight, len(items))
    res = [[0 for i in range(size[0] + 1)] for j in range(size[1] + 1)]
    for i in range(size[1] + 1):
        for x in range(size[0] + 1):
            if i == 0 or x == 0:
                res[i][x] = 0
            elif items[i - 1][1] <= x:
                tmp1 = res[i - 1][x]
                tmp2 = res[i - 1][x - items[i - 1][1]] + items[i - 1][0]
                tmp3 = max(tmp1, tmp2)
                res[i][x] = tmp3
            else:
                res[i][x] = res[i - 1][x]

    ######
    total_value = res[size[1]][size[0]]
    i = size[1]
    while i > 0:
        if res[i][total_weight] > res[i - 1][total_weight]:
            result_items.append(i - 1)
            total_weight -= items[i - 1][1]
        i -= 1
    ######
    return total_value, result_items


dct = {}


def knapsack_new(items: list, total_weight, n=0):
    """
    :param total_weight:
    :param items: (value, weight)
    :return:
    """
    if total_weight < 0:
        return -999999999
    if n < 0 or total_weight == 0:
        return 0
    key = str(len(items)) + '|' + str(total_weight)

    if not key in dct:
        tmp = items[len(items)] + knapsack_new(items, total_weight, n)

    size = (total_weight, len(items))
    res = [[0 for i in range(size[0] + 1)] for j in range(size[1] + 1)]
    for i in range(size[1] + 1):
        for x in range(size[0] + 1):
            if i == 0 or x == 0:
                res[i][x] = 0
            elif items[i - 1][1] <= x:
                tmp1 = res[i - 1][x]
                tmp2 = res[i - 1][x - items[i - 1][1]] + items[i - 1][0]
                tmp3 = max(tmp1, tmp2)
                res[i][x] = tmp3
            else:
                res[i][x] = res[i - 1][x]

    ######
    total_value = res[size[1]][size[0]]
    i = size[1]
    while i > 0:
        if res[i][total_weight] > res[i - 1][total_weight]:
            result_items.append(i - 1)
            total_weight -= items[i - 1][1]
        i -= 1
    ######
    return total_value, result_items


if __name__ == '__main__':
    with open('tmp.json') as file:
        data = json.loads(file.read())
        items1 = data[0]['items']
        items2 = data[1]['items']
        res1 = data[0]['result']
        res2 = data[1]['result']
        weight1 = data[0]['weight']
        weight2 = data[1]['weight']
        print(knapsack(items2, weight2))
        print(knapsackbitmask(items2, weight2))
        # print(data[0])
        # print(data[1])
