from reader import FileReader
from task_07 import Solver

from optparse import OptionParser

DEBUG = False

def scenario_A(file_in):
    print("Input file: {}".format(file_in))

    global DEBUG
    reader = FileReader(file_in)
    problem = reader.read()

    solver = Solver(problem)
    print("Description:")
    print(solver.description())

    solution = solver.initial_solution()
    # print(solver.initial_solution().print_free())
    # print("-------")
    # print(solver.initial_solution().print_solution())
    # print("here")
    # print("\n".join(str(i) for i in solver.initial_solution().slices))
    # print("here2")
    print("Initial solution score: {}".format(solution.score()))
    if DEBUG:
        solution.print_solution()

    optimized_solution = solver.search(solution, time_limit=60)
    print("Optimized solution score: {}".format(optimized_solution.score()))
    # print("\n".join(str(i) for i in optimized_solution.slices))
    if DEBUG:
        optimized_solution.print_solution()

    trace = solver.get_search_trace()
    if trace is not None:
        print("Trace:")
        print("\n".join([str(x) for x in trace]))


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--input-file", dest="in_file", help="Input file name", metavar="FILE")
    parser.add_option("-o", "--output-file", dest="out_file", help="Output file name", metavar="FILE")
    parser.add_option("-p", "--param-file", dest="par_file", help="Parameters' file name", metavar="FILE", default=None)
    parser.add_option("-d", "--debug", action="store_true", help="Debug mode ON", default=False)
    (options, args) = parser.parse_args()

    DEBUG = options.debug
    scenario_A("not_that_big.in")
