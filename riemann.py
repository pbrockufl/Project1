import numpy as np

def left_endpoint(x_values: np.ndarray, func: np.ufunc):
    widths = np.diff(x_values)
    heights = func(x_values[:-1])
    areas = widths * heights
    return np.sum(areas)

def trapezoid(x_values: np.ndarray, func: np.ufunc):
    widths = np.diff(x_values)
    heights = (func(x_values[:-1]) + func(x_values[1:])) / 2
    areas = widths * heights
    return np.sum(areas)

def simpson(x_values: np.ndarray, func: np.ufunc):
    n = len(x_values) - 1 #Subintervals
    Sum = 0
    for i in range(0, n, 2): #Step size 2
        a, b, c = x_values[i], x_values[i+1], x_values[i+2]
        h = (c-a) / 2 #Half interval

        Sum += (c-a) / 6 * (func(a) + 4 * func(b) + 4 * func(c))
    return Sum
