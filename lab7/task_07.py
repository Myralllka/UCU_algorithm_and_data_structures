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
        raise Exception("Implement your search procedure")
        return optimized_solution

    def get_search_trace(self):
        return self.trace