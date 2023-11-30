import numpy as np


def easom(x: float, y: float) -> float:
    """
    Calculate the value of Easom function at point (x, y)

    :param x: x coordinate
    :param y: y coordinate
    :return: value of Easom function at point (x, y)
    """
    return -(np.cos(x) * np.cos(y) * np.exp(-(x - np.pi) ** 2 - (y - np.pi) ** 2))
