from init_solver import InitSolverSilly
from solution import Solution


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
        return "I Just go throw all slices from the initial solution " \
               "and try to make it bigger either in right or in down"

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
        optimized_solution: Solution
        optimized_solution = solution.duplicate()
        for sl in optimized_solution.get_all_slices():
            if optimized_solution.p.is_valid_slice(sl[0], sl[1], sl[2] + 1, sl[3]):
                if optimized_solution.is_free_space(sl[0] + sl[2], sl[1], 1, sl[3]):
                    optimized_solution.delete_slice(sl[0], sl[1])
                    optimized_solution.create_new_slice(sl[0], sl[1], sl[2] + 1, sl[3])
            elif optimized_solution.p.is_valid_slice(sl[0], sl[1], sl[2], sl[3] + 1):
                if optimized_solution.is_free_space(sl[0], sl[1] + sl[3], sl[2], 1):
                    optimized_solution.delete_slice(sl[0], sl[1])
                    optimized_solution.create_new_slice(sl[0], sl[1], sl[2], sl[3] + 1)
        Solver.trace = [optimized_solution.score()]
        return optimized_solution

    def get_search_trace(self):
        return self.trace
