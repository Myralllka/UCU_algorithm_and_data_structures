def max_billbords(billbords, values, m):
    max_profit = [0] * (m + 1)
    next_bb = 0
    max_profit[0] = 0
    step = 5
    for i in range(m):
        if next_bb < len(billbords):
            if billbords[next_bb] != i:
                max_profit[i] = max_profit[i - 1]
            else:
                if i >= step:
                    max_profit[i] = max(max_profit[i - step] + values[next_bb],
                                        max_profit[i - 1])
                else:
                    max_profit[i] = values[next_bb]

                next_bb += 1
        else:
            max_profit[i] = max_profit[i - 1]
        print(max_profit)
    return max_profit[m - 1]


print(max_billbords([1, 2, 3, 4, 5, 6], [5, 1, 1, 1, 1, 7], 15))
