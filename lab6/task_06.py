import copy
from queue import Queue
from collections import deque


def bfs(gr, i, j):
    pass


def dfs(gr):
    pass


def escape_problem_max_flow(lst):
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


def escape_problem(lst):
    def bfs(matrix, i, j):
        if i in contour or j in contour:
            return [[i, j]]
        parents = {}
        q = Queue()
        q.put((i, j))
        res = []
        flag = False
        while not q.empty():
            tmp = q.get()
            if tmp[0] in contour or tmp[1] in contour:
                flag = True
                break
            for each in neighbours:
                if (0 <= tmp[0] + each[0] < len(matrix) and 0 <= tmp[1] + each[1] < len(matrix) and
                        matrix[tmp[0] + each[0]][tmp[1] + each[1]] != 1):
                    parents[(tmp[0] + each[0], tmp[1] + each[1])] = (tmp[0], tmp[1])
                    matrix[tmp[0] + each[0]][tmp[1] + each[1]] = 1
                    q.put((tmp[0] + each[0], tmp[1] + each[1]))
        if flag:
            while True:
                try:
                    res.append((tmp[0], tmp[1]))
                    tmp = parents[(tmp[0], tmp[1])]
                except KeyError:
                    break
            return res[::-1]

    array = copy.deepcopy(lst)
    result = list()
    contour = [0, len(lst) - 1]
    neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for i in range(len(array)):
        for j in range(len(array)):
            if lst[i][j] == 1:
                result.append(bfs(copy.deepcopy(array), i, j))
                try:
                    for each in result[-1]:
                        array[each[0]][each[1]] = 1
                except:
                    result.pop()
    return result


if __name__ == "__main__":
    print(escape_problem([[0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1]]))
