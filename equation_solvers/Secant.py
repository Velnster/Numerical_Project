from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root


class Secant(EquationSolver):
    DEFAULT_FIRST_INITIAL_POINT = -1
    DEFAULT_SECOND_INITIAL_POINT = 0

    def __init__(self, equation,first_initial_point=DEFAULT_FIRST_INITIAL_POINT,
                 second_initial_point=DEFAULT_SECOND_INITIAL_POINT ,max_iterations = EquationSolver.DEFAULT_MAX_ITERATIONS , precision = EquationSolver.DEFAULT_EPSILON):
        super().__init__(equation)
        self.first_initial_point = first_initial_point
        self.second_initial_point = second_initial_point
        self.max_iterations = max_iterations
        self.precision = precision

    def start_root_finding(self):

        #self.add_root(Root(self.calculate_root(self.first_initial_point, self.second_initial_point), None))
        temp_root = Root (self.second_initial_point,0)
        self.roots.append(temp_root)
        temp_root = Root (self.first_initial_point,0)
        self.roots.append(temp_root)
        old_root = self.second_initial_point
        current_root = self.roots[-1].root
        new_root = self.calculate_root(old_root, current_root)
        new_precision = self.calculate_precision(current_root, new_root)

        self.add_root(Root(new_root, new_precision))

        if self.roots[-1].precision <= self.precision:
            self.root_found = True

        else:
            counter = 2

            while self.roots[-1].precision > self.precision and counter <= self.max_iterations:
                old_root = self.roots[-2].root
                current_root = self.roots[-1].root
                new_root = self.calculate_root(old_root, current_root)
                new_precision = self.calculate_precision(current_root, new_root)
                self.add_root(Root(new_root, new_precision))
                counter += 1

            if self.roots[-1].precision <= self.precision:
                self.root_found = True

    def calculate_root(self, old_root, current_root) -> float:
        old_value = self.evaluate_equation(old_root)
        new_value = self.evaluate_equation(current_root)
        return (current_root - (new_value * ((current_root - old_root) / (
                new_value - old_value))))
