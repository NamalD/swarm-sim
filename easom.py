import numpy as np


def easom(x, y):
    return -(np.cos(x) * np.cos(y) * np.exp(-(x - np.pi) ** 2 - (y - np.pi) ** 2))
