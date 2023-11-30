import math


def easom(x, y):
    -math.cos(x) * math.cos(y) * math.exp(-math.pow((x - math.pi), 2) -math.pow((y - math.pi), 2))
