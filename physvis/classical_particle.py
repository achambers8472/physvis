import numpy as np


class ClassicalParticle:
    def __init__(self, x, v, m=1):
        self.x = np.asanyarray(x)
        self.v = np.asanyarray(v)
        self.m = m

    def update(self, F, dt):
        self.v += (F/self.m)*(dt/2)
        self.x += self.v*dt
        self.v += (F/self.m)*(dt/2)

    def draw(self, canvas):
        canvas.draw_point(self.x.astype(int))
