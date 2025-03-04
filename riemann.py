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
    #(b-a)/2 (f(a) + 4((a-b)/2) + f(b))
    n = len(x_values) # Calculates intervals
    Sum = 0
    for i in range(0, n-2, 2): #Step size 2
        a, b, c = x_values[i], x_values[i+1], x_values[i+2] #Values within interval

        Sum += (c-a) / 6 * (func(a) + 4 * func(b) + func(c)) #Simpsons function
    return Sum
