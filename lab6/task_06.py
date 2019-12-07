import copy


def escape_problem(lst):
    graph = {"start": [], "end": []}
    contour = [0, len(lst) - 1]
    matrix = copy.deepcopy(lst)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                graph["{} {} out".format(i, j)] = []
            else:
                graph["{} {} in".format(i, j)] = ["{} {} out".format(i, j)]
                graph["{} {} out".format(i, j)] = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i in contour or j in contour:
                graph["{} {} out".format(i, j)].append("end")
                if matrix[i][j] == 1:
                    graph["start"].append("{} {} in".format(i, j))
            # elif (i == len(lst) - 1 and j != 0) or (j == len(lst) - 1 and i != 0):
            if i > 0 and j > 0:
                try:
                    if "{} {} in".format(i - 1, j) in graph:
                        graph["{} {} out".format(i, j)].append("{} {} in".format(i - 1, j))
                except AttributeError:
                    pass
                try:
                    if "{} {} in".format(i, j - 1) in graph:
                        graph["{} {} out".format(i, j)].append("{} {} in".format(i, j - 1))
                except AttributeError:
                    pass
                try:
                    if "{} {} in".format(i, j) in graph:
                        graph["{} {} out".format(i - 1, j)].append("{} {} in".format(i, j))
                except AttributeError:
                    pass
                try:
                    if "{} {} in".format(i, j) in graph:
                        graph["{} {} out".format(i, j - 1)].append("{} {} in".format(i, j))
                except AttributeError:
                    pass

    return graph


if __name__ == "__main__":
    escape_problem([[0, 0, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1]])
