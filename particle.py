from vector import Vector


class Particle:
    def __init__(self, min_bound, max_bound):
        self.position = Vector.random(min_bound, max_bound)
        self.velocity = Vector.random(min_bound, max_bound)

    # TODO: Unit test this method.
    def update(self):
        # TODO: Update the particle's velocity.
        self.position += self.velocity
        # TODO: Update the particle's best-known position and fitness value.
        # TODO: Update the global best-known position and fitness value.
        pass

