import numpy as np

from . import wavefunction


class ClassicalParticle:
    def __init__(self, x, pos, vel, mass=1):
        self.x = x
        self.pos = np.asanyarray(pos, dtype=float)
        self.vel = np.asanyarray(vel, dtype=float)
        self.mass = mass
        self._acc = np.zeros((2,))

    def update(self, F, dt):
        acc = F/self.mass
        self.vel += acc*(dt/2)
        self.pos += self.vel*dt
        self.vel += acc*(dt/2)
        self._acc = acc

    def draw(self, canvas):
        y = np.asanyarray(canvas.size)
        sc = y/(self.x[-1, -1] - self.x[0, 0])
        act = ((self.pos - self.x[0, 0])*sc).astype(int)
        canvas.draw_point(act, max(int(self.mass), 1))
        canvas.draw_line(act, (act + self.vel*sc*0.1).astype(int))
        canvas.draw_line(act, (act + self._acc*sc*0.01).astype(int), (0, 255, 0, 255))
