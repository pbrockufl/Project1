import numpy as np

def left_endpoint(x_values, func):
    widths = np.diff(x_values)
    heights = func(x_values[:-1])
    areas = widths * heights
    return np.sum(areas)

def trapezoid(x_values, func):
    widths = np.diff(x_values)
    heights = (func(x_vals[:-1]) + func(x_vals[1:])) / 2
    areas = widths * heights
    return np.sum(areas)
