import numpy as np

from . import space


def checksum(psi):
    return (np.abs(psi)**2).sum()


class QuantumParticle:
    def __init__(self, x, wf, m=1):
        self.m = m
        self.x = x
        self.wf = wf
        self.V = np.zeros_like(wf)
        N = len(self.x)
        dk = (2*np.pi)/(self.x[-1, 0, 0] - self.x[0, 0, 0])
        print(dk)
        self.k = space.isotropic(N, dk)

    def update(self, dt):
        wf_half = self.wf*np.exp(-1j*self.V*dt/2)
        wf_k = np.fft.fft2(wf_half)/len(wf_half)

        new_wf_k = wf_k*np.exp(-1j*(self.k**2).sum(axis=-1)*dt/(2*self.m))
        new_wf_half = np.fft.ifft2(new_wf_k)*len(new_wf_k)

        new_wf = new_wf_half*np.exp(-1j*self.V*dt/2)

        self.wf = new_wf


    def draw(self, canvas):
        p = np.abs(self.wf)**2
        canvas.draw_map(self.x, p/p.max())
