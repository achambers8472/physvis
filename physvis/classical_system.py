class ClassicalSystem:
    def __init__(self, particles, forces):
        self.particles = particles
        self.forces = forces

    def update(self, dt):
        Fs = np.zeros((len(self.particles), 2))
        for force in self.forces:
            Fs = force(particles)
        for F, particle in zip(Fs, self.particles):
            particle.update(F, dt)

    def draw(self, canvas):
        for particle in self.particles:
            particle.draw(canvas)
