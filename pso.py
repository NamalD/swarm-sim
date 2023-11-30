from particle import Particle


class PSO:
    def __init__(self, particle_count: int, min: int, max: int, fitness_function):
        # Initialize a swarm of particles with random positions and velocities.
        self.particles = [Particle(min, max) for _ in range(particle_count)]
        self.fitness_function = fitness_function

        # TODO: Set the best-known positions for each particle and the global best-known position.
        # TODO: Set the best-known fitness values for each particle and the global best-known fitness value.

    def update(self):
        for particle in self.particles:
            particle.update()

        # TODO: Apply constraints if necessary to keep particles within a valid solution space.
        # TODO: Update the global best-known position and fitness value.
        return True

    def best(self):
        # Return the best-known position and fitness value for the swarm.
        pass

    def terminate(self):
        # Terminate the algorithm when a stopping criterion is met.
        pass

    def run(self):
        # Run the algorithm until the stopping criterion is met.
        pass
