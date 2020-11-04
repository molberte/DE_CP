from numeric_methods.functions import Functions
from numeric_methods.exact_solution import ExactSolution
from numeric_methods.euler_method import EulerMethod
from numeric_methods.improved_euler_method import ImprovedEulerMethod
from numeric_methods.runge_kutta_method import RungeKuttaMethod
from error_calculator.local_errors import LocalErrors


class TotalErrors:
    @staticmethod
    def calculate(local_errors, n0, nmax):
        total_errors = [max(map(abs, error)) for _, error in local_errors]
        grid_cells = range(n0, nmax + 1)

        return grid_cells, total_errors

    def calculate_local_errors(self, x_init, y_init, x_max, n_approx, n0, nmax, class_derived):
            local_errors = []
            # euler_local_errors = []
            # improved_euler_local_errors = []
            # runge_kutta_local_errors = []

            for i in range(n0, nmax + 1):
                exact_points = ExactSolution.solve(x_init, y_init, x_max, n_approx, Functions.exact_solution)
                points = class_derived.solve(x_init, y_init, x_max, n_approx, Functions.initial_equation)
                local_error_points = LocalErrors.calculate(exact_points, points)
                local_errors.append(local_error_points)

                return local_errors

                # exact_points = ExactSolution.solve(x_init, y_init, x_max, n_approx, Functions.exact_solution)
                # euler_points = EulerMethod.solve(x_init, y_init, x_max, n_approx, Functions.initial_equation)
                # improved_euler_points = ImprovedEulerMethod.solve(x_init, y_init, x_max, n_approx,
                #                                                   Functions.initial_equation)
                # runge_kutta_points = RungeKuttaMethod.solve(x_init, y_init, x_max, n_approx, Functions.initial_equation)
                #
                # euler_local_error_points = LocalErrors.calculate(exact_points, euler_points)
                # improved_euler_local_error_points = LocalErrors.calculate(exact_points, improved_euler_points)
                # runge_kutta_local_error_points = LocalErrors.calculate(exact_points, runge_kutta_points)
                #
                # euler_local_errors.append(euler_local_error_points)
                # improved_euler_local_errors.append(improved_euler_local_error_points)
                # runge_kutta_local_errors.append(runge_kutta_local_error_points)

            # euler_total_error_points = self.pre_calculate(euler_local_errors, n0, nmax)
            # improved_euler_total_error_points = self.pre_calculate(improved_euler_local_errors, n0, nmax)
            # runge_kutta_total_error_points = self.pre_calculate(runge_kutta_local_errors, n0, nmax)

            # return euler_total_error_points, improved_euler_total_error_points, runge_kutta_total_error_points
