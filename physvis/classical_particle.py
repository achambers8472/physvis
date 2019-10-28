import numpy as np

from . import wavefunction


class ClassicalParticle:
    def __init__(self, x, pos, vel, mass=1):
        self.x = x
        self.pos = np.asanyarray(pos, dtype=float)
        self.vel = np.asanyarray(vel, dtype=float)
        self.mass = mass

    def update(self, F, dt):
        self.vel += (F/self.mass)*(dt/2)
        self.pos += self.vel*dt
        self.vel += (F/self.mass)*(dt/2)

    def draw(self, canvas):
        y = np.asanyarray(canvas.size)
        act = ((self.pos - self.x[0, 0])/(self.x[-1, -1] - self.x[0, 0])*y).astype(int)
        canvas.draw_point(act)
