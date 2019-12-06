import copy


class Node:
    def __init__(self, value, coordinates=(-1, -1), typee=None):
        """
        typee = vin, vout, contour;
        value = 0 or 1;
        """
        self.out_node = None
        self.value = value
        self.neighbours = []
        self.dots = []
        self.typee = typee
        self.coordinates = coordinates

    def add_neighbor_in(self, node):
        if self.typee == "vout":
            raise IndexError("FUCK")
        self.neighbours.append(node)

    def add_neighbour_out(self, node):
        if self.typee == "vin":
            raise IndexError("FUCK")
        self.neighbours.append(node)

    def __eq__(self, other):
        return self.coordinates == other.coordinates and self.typee == \
               other.typee


def escape_problem(lst):

    def matrix_to_graph(matr):
        st_node = Node(1, typee="vout")
        en_node = Node(0, typee="vin")
        for i in range(len(matr)):
            for j in range(len(matr)):
                if i in contour or j in contour:
                    end_node.add_neighbor_in(matrix[i][j])
                    if matrix[i][j].value == 1:
                        start_node.add_neighbour_out(matrix[i][j])
        return start_node, end_node

    contour = [0, len(lst) - 1]
    neigbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    matrix = copy.deepcopy(lst)

    """
    Make a matrix of Nodes
    """
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = Node(matrix[i][j], (i, j))

    start_node, end_node = matrix_to_graph(matrix)


if __name__ == "__main__":
    escape_problem([[1, 0, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 0]])
