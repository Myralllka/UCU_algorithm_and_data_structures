from init_solver import InitSolverSilly

import time


class Solver:
    problem = None
    trace = None

    def __init__(self, problem):
        self.problem = problem

    def description(self):
        """
        :return: String with the description of the approach
        """
        # TODO: Place your algorithm's description here
        return ""

    def initial_solution(self):
        """
        Finds an initial solution for the problem
        :return: Solution object
        """
        # TODO: If you want you may change an initial solution generation
        init_solver = InitSolverSilly()
        solution = init_solver.run(self.problem)
        return solution

    def search(self, solution, time_limit=float('inf')):
        """
        Runs a search to optimize the solution. The run is limited by time limit (in seconds)
        :param solution: the initial solution object
        :param time_limit: run time limit (in seconds)
        :return: Solution object after optimization, list of the traced solutions' score
        """

        # TODO: implement your search procedure. Do not forget about time limit!
        def get_neighbours(x, y, maxx, maxy):
            res = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for var in res:
                if 0 < x + var[0] <= maxx or 0 < y + var[0] <= maxy:
                    res.remove(var)
                    continue
            return res

        init_time = time.time()
        optimized_solution = solution.duplicate()
        print("\n".join([str(i) for i in optimized_solution.free]))
        while time.time() - init_time < 120:
            for i in range(len(optimized_solution.free)):
                for j in range(len(optimized_solution[0])):
                    prev_solution = optimized_solution.duplicate()
                    
                    # for neighbour in get_neighbours(i, j, len(optimized_solution.free), len(optimized_solution.free[0])):
                    #     optimized_solution.delete_slice(i + neighbour[0], i + neighbour[1])
                    #     if (optimized_solution.is_free_space(i + neighbour[0], i + neighbour[1], ))
                    #         optimized_solution.create_new_slice()


        return optimized_solution

    def get_search_trace(self):
        return self.trace
