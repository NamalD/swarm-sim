import random


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def random(min_bound: float, max_bound: float):
        return Vector(
            random.uniform(min_bound, max_bound),
            random.uniform(min_bound, max_bound)
        )
