import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    x1, x2, x3 = triangle_coordinates[0] # extracts x-coord of triangle vertices
    y1, y2, y3 = triangle_coordinates[1] # extracts y-coord of triangle vertices
    x, y = point_coordinates
    denom = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1- y3)

    if abs(denom) < 1e-10: # determinant
        return np.array([-1, -1, -1])
    # computes barycentric coordinates
    lambda1 = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denom
    lambda2 = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denom
    lambda3 = 1 - lambda1 - lambda2

    return np.array([lambda1, lambda2, lambda3])

def get_cartesian_coordinates(triangle_coordinates: np.ndarray, bar_coordinates: np.ndarray) -> np.ndarray:
    return np.dot(triangle_coordinates, bar_coordinates) # matrix multiplication

def is_inside_triangle(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> bool:
    bar_coordinates = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    if np.any(bar_coordinates < -0.01):
        return False
    return np.all(bar_coordinates >= 0)
