import numpy as np


class QuantumParticle:
    def __init__(self, x, wf, m=1):
        self.m = m
        self.x = x
        self.wf = wf
        self.V = np.zeros_like(x)

    def update(self, dt):
        pass
        # new_v = self.v + (self.F/self.m)*(dt)
        # v_half = (new_v + self.v)/2
        # new_x = self.x + v_half*dt

        # self.x = new_x
        # self.v = new_v

    def draw(self, canvas):
        print(f'drawing self at {self.x}')
        canvas.draw_map(self.x, self.wf)
