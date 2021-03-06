from sympy import Symbol, Derivative, simplify

from equation_solvers import Root


class EquationSolver:
    precision = 0.0
    max_iterations =  0
    equation = ""
    root_found = False
    roots = []

    DEFAULT_MAX_ITERATIONS = 50
    DEFAULT_EPSILON = 0.0001

    @staticmethod
    def get_first_derivative(equation: str, value) -> float:
        x = Symbol('x')
        return Derivative(equation, x).doit().subs({x: value})

    @staticmethod
    def get_second_derivative(equation: str, value) -> float:
        x = Symbol('x')
        first_deriv = Derivative(equation, x).doit()
        return Derivative(first_deriv, x).doit().subs({x: value})

    def evaluate_equation(self, value_to_substitute) -> float:
        simple_equation = simplify(self.equation)
        return simple_equation.subs("x", value_to_substitute).evalf()

    def __init__(self, equation, max_iterations=DEFAULT_MAX_ITERATIONS, precision=DEFAULT_EPSILON):
        self.equation = equation
        self.max_iterations = max_iterations
        self.precision = precision
        self.roots = []
        self.root_found = False

    def next_iteration(self) -> bool:

        pass

    def add_root(self, new_root: Root):
        self.roots.append(new_root)

    def delete_root(self, root_to_delete: Root):
        self.roots.remove(root_to_delete)

    @property
    def max_iterations(self):
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        if max_iterations > 0:
            self._max_iterations = max_iterations
        else:
            self._max_iterations = self.DEFAULT_MAX_ITERATIONS

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, precision):
        if precision > 0:
            self._precision = precision
        else:
            self._precision = self.DEFAULT_EPSILON

    def calculate_precision(self, old_root, new_root) -> float:
        return abs((new_root - old_root) / new_root)
