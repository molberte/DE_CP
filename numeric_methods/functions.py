from math import exp


def const(x, y):
    return (y + x ** 2 + 1) / exp(x ** 2)

class Functions:
    @staticmethod
    def initial_equation(x, y):
        return 2 * x * (x ** 2 + y)

    @staticmethod
    def exact_solution(x, x0, y0):
        return -x ** 2 - 1 + const(x0, y0) * exp(x ** 2)
