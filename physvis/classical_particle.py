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
        print(f"Drawing classical particle at {self.pos}")
        dxs = self.x[1, 1] - self.x[0, 0]
        array = wavefunction.wavepacket(
            (0, 0),
            self.pos,
            dxs[0],
            self.x,
        )
        array = (np.abs(array)**2)*dxs.prod()
        canvas.draw_array((0, 0), array/0.001)
        # canvas.draw_point(self.pos.astype(int))
