import numpy as np


class ClassicalParticle:
    def __init__(self, x, v, m=1):
        self.m = m
        self.x = np.asanyarray(x)
        print(self.x)
        self.v = np.asanyarray(v)
        self.F = np.zeros_like(v)

    def update(self, dt):
        new_v = self.v + (self.F/self.m)*(dt)
        v_half = (new_v + self.v)/2
        new_x = self.x + v_half*dt

        self.x = new_x
        self.v = new_v

    def draw(self, canvas):
        print(f'drawing self at {self.x}')
        canvas.draw_point(self.x.astype(int))
