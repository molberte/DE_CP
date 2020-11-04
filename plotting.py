import matplotlib
from matplotlib import pyplot as plt
from numeric_methods.functions import Functions
from numeric_methods.exact_solution import ExactSolution
from numeric_methods.euler_method import EulerMethod
from numeric_methods.improved_euler_method import ImprovedEulerMethod
from numeric_methods.runge_kutta_method import RungeKuttaMethod
from error_calculator.local_errors import LocalErrors
from error_calculator.total_errors import TotalErrors
import pandas as np


class Points:
    def __init__(self, x_init, y_init, x_max, n_approx, n_0, n_max):
        self.exact_points = ExactSolution.solve(x_init, y_init, x_max, n_approx, Functions.exact_solution)
        self.euler_points = EulerMethod.solve(x_init, y_init, x_max, n_approx, Functions.initial_equation)
        self.improved_euler_points = ImprovedEulerMethod.solve(x_init, y_init, x_max, n_approx, Functions.initial_equation)
        self.runge_kutta_points = RungeKuttaMethod.solve(x_init, y_init, x_max, n_approx, Functions.initial_equation)

        self.euler_local_error_points = LocalErrors.calculate(self.exact_points, self.euler_points)
        self.improved_euler_local_error_points = LocalErrors.calculate(self.exact_points, self.improved_euler_points)
        self.runge_kutta_local_error_points = LocalErrors.calculate(self.exact_points, self.runge_kutta_points)



class Plot(Points):
    @staticmethod
    def plot(x_init, y_init, x_max, n_approx, n_0, n_max):
        points = Points(x_init, y_init, x_max, n_approx, n_0, n_max)
        fig = plt.figure()
        ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
        ax1.plot(*points.euler_points, label="Euler")
        ax1.plot(*points.improved_euler_points, label="Improved Euler")
        ax1.plot(*points.runge_kutta_points, label="Runge Kutta")
        ax1.plot(*points.exact_points, label="Exact solution")
        ax1.set_xlabel('x axis')  # Add an x-label to the axes
        ax1.set_ylabel('y axis')  # Add a y-label to the axes
        ax1.set_title("Approximation")  # Add a title to the axes.
        ax1.legend()
        ax1.grid()

        ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
        ax2.plot(*points.euler_points, label="Euler")
        ax2.plot(*points.improved_euler_points, label="Improved Euler")
        ax2.plot(*points.runge_kutta_points, label="Runge Kutta")
        ax2.plot(*points.exact_points, label="Exact solution")
        ax2.set_xlabel('x axis')  # Add an x-label to the axes
        ax2.set_ylabel('y axis')  # Add a y-label to the axes
        ax2.set_title("Approximation")  # Add a title to the axes.
        ax2.legend()
        ax2.grid()

        plt.tight_layout()
        plt.show()
