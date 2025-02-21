import numpy as np

def left_endpoint(x_values: np.ndarray, func: np.ufunc):
    widths = np.diff(x_values)
    heights = func(x_values[:-1])
    areas = widths * heights
    return np.sum(areas)

def trapezoid(x_values: np.ndaraay, func: np.ufunc):
    widths = np.diff(x_values)
    heights = (func(x_values[:-1]) + func(x_values[1:])) / 2
    areas = widths * heights
    return np.sum(areas)
