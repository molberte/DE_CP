from math import exp


def const(x, y):
    return (y + x ** 2 + 1) / exp(x ** 2)


class Functions:
    @staticmethod
    def solve(x0, y0, xmax, n, func):
        raise NotImplementedError

    @staticmethod
    def initial_equation(x, y):
        return 2 * x * (x ** 2 + y)

    @staticmethod
    def exact_solution(x, x0, y0):
        return -x ** 2 - 1 + const(x0, y0) * exp(x ** 2)

    @staticmethod
    def calculate(local_errors, n0, nmax):
        total_errors = [max(map(abs, error)) for _, error in local_errors]
        grid_cells = range(n0, nmax + 1)

        return grid_cells, total_errors

    def calculate_local_errors(self, x_init, y_init, x_max, n_approx, n0, nmax):
        from numeric_methods.exact_solution import ExactSolution
        from error_calculator.local_errors import LocalErrors

        local_errors = []

        for i in range(n0, nmax + 1):
            exact_points = ExactSolution.solve(x_init, y_init, x_max, n_approx, Functions.exact_solution)
            points = self.solve(x_init, y_init, x_max, n_approx, Functions.initial_equation)
            local_error_points = LocalErrors.calculate(exact_points, points)
            local_errors.append(local_error_points)

            return local_errors
