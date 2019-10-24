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

    def update(self, dt):
        wf_half = self.wf*np.exp(-1j*self.V*dt/2)
        wf_k = np.fft.fft2(wf_half)/len(wf_half)

        n_k = self.x.shape[:-1]
        dk = (2*np.pi)/(self.x[-1, -1] - self.x[0, 0])

        nk = n_k[0]
        dk = dk[0]

        k = space.isotropic(nk, dk)

        new_wf_k = wf_k*np.exp(-1j*(k**2).sum(axis=-1)*dt/(2*self.m))

        new_wf_half = np.fft.ifft2(new_wf_k)*len(new_wf_k)

        new_wf = new_wf_half*np.exp(-1j*self.V*dt/2)

        self.wf = new_wf


    def draw(self, canvas):
        p = np.abs(self.wf)**2
        canvas.draw_map(self.x, p/p.max())
