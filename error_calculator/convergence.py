from numeric_methods.functions import Functions
from numeric_methods.exact_solution import ExactSolution
from numeric_methods.euler_method import EulerMethod
from numeric_methods.improved_euler_method import ImprovedEulerMethod
from numeric_methods.runge_kutta_method import RungeKuttaMethod


class Convergence:
    @staticmethod
    def compute_error(method1, method2):  # compute difference between numerical method and exact solution at each step
        m = len(method1)
        answer = m * [0]
        for i in range(m):
            answer[i] = abs(method1[i] - method2[i])
        return answer

    def calculate_convergence(self, x_init, y_init, x_max, n0, nmax):
        total_errors_e = []  # Euler
        total_errors_ie = []  # Improved Euler
        total_errors_rk = []  # Runge-Kutta
        base_solver = Functions()
        exact_solver = ExactSolution()
        euler_solver = EulerMethod()
        improved_euler_solver = ImprovedEulerMethod()
        runge_kutta_solver = RungeKuttaMethod()

        for i in range(n0, nmax):
            # values of exact solution and numerical methods when we use i computational steps
            exact_i = exact_solver.solve(x_init, y_init, x_max, i, base_solver.exact_solution)
            euler_i = euler_solver.solve(x_init, y_init, x_max, i,  base_solver.initial_equation)
            improved_i = improved_euler_solver.solve(x_init, y_init, x_max, i, base_solver.initial_equation)
            runge_kutta_i = runge_kutta_solver.solve(x_init, y_init, x_max, i, base_solver.initial_equation)

            # compute their errors
            euler_error_i = self.compute_error(exact_i[1], euler_i[1])
            improved_euler_error_i = self.compute_error(exact_i[1], improved_i[1])
            runge_kutta_error_i = self.compute_error(exact_i[1], runge_kutta_i[1])

            # append average values of errors
            total_errors_e.append(max(map(abs, euler_error_i)))
            total_errors_ie.append(max(map(abs, improved_euler_error_i)))
            total_errors_rk.append(max(map(abs, runge_kutta_error_i)))

        return [total_errors_e, total_errors_ie, total_errors_rk]
