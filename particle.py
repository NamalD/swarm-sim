from vector import Vector


class Particle:
    def __init__(self, min_bound, max_bound):
        self.position = Vector.random(min_bound, max_bound)
        self.velocity = Vector.random(min_bound, max_bound)

