import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    x, y = point_coordinates

    denom = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    lamda1 = ((x2 - x) * (y3 - y) - (x3 - x) * (y2 - y)) / denom
    lamda2 = ((x3 - x) * (y1 - y) - (x1 - x) * (y3 - y)) / denom
    lamda3 = 1 - lamda1 - lamda2

    return np.array([lamda1, lamda2, lamda3])

def get_cartesian_coordinates(triangle_coordinates: np.ndarray, barycentric_coordinates: np.ndarray) -> np.ndarray:
    return np.dot(triangle_coordinates, barycentric_coordinates)

import numpy as np

def is_inside_triangle(triangle_coordinates, point_coordinates):
  bar_coordinates = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
  return np.all(bar_coordinates >= 0)

