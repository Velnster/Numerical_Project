from equation_solvers.EquationSolver import EquationSolver


class NewtonRaphson(EquationSolver):

    # Add suitable args
    def __init__(self, equation):
        super().__init__(equation)
