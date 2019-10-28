import numpy as np

class QuantumSystem:
    def __init__(self, particles, potential):
        self.particles = particles
        self.potential = potential

    def update(self, dt):
        for particle in self.particles:
            particle.update(self.potential, dt)

    def draw(self, canvas):
        for particle in self.particles:
            particle.draw(canvas)
        canvas.draw_array(
            (0, 0),
            self.potential/self.potential.max(),
            mask=(self.potential != 0),
            color_map='Greys_r',
            alpha=0.5,
        )
