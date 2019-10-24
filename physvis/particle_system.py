class ParticleSystem:
    def __init__(self, particles):
        self.particles = particles

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)

    def draw(self, canvas):
        print(f'drawing {self} on {canvas}')
        for particle in self.particles:
            particle.draw(canvas)
