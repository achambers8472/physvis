import time


class ParticleSystem:
    def __init__(self, particles):
        self.particles = particles

    def update(self, dt):
        start = time.time()
        for particle in self.particles:
            particle.update(dt*0.1)
        print('Update time:', time.time() - start)

    def draw(self, canvas):
        for particle in self.particles:
            particle.draw(canvas)
