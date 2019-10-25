import numpy as np

from . import space


def normsq(psi):
    return np.abs(psi)**2


class QuantumParticle:
    def __init__(self, x, psi, m=1):
        self.m = m
        self.x = x
        self.psi = psi
        self.V = np.zeros_like(psi)
        self.dxs = self.x[1, 1] - self.x[0, 0]

        Ns = self.x.shape[:-1]
        self.dks = (2*np.pi)/(Ns*self.dxs)
        self.k = space.normal(Ns, self.dks)
        k0 = self.k[0, 0]

        self._k0_dot_x = (k0*self.x).sum(axis=-1)
        self._mod_factor = np.exp(-1j*self._k0_dot_x)*self.dxs[0]/(2*np.pi)
        self._unmod_factor = np.exp(1j*self._k0_dot_x)*(2*np.pi)/self.dxs[0]
        self._k2 = (self.k**2).sum(axis=-1)

    def update(self, dt):
        psi_x = self.psi
        x_half_up_factor = np.exp((-0.5j*dt)*self.V)

        psi_mod_x = psi_x*self._mod_factor
        psi_mod_x *= x_half_up_factor

        psi_mod_k = np.fft.fft2(psi_mod_x)
        psi_mod_k *= np.exp((-0.5j*dt/self.m)*self._k2)
        psi_mod_x = np.fft.ifft2(psi_mod_k)

        psi_mod_x *= x_half_up_factor
        psi_x = psi_mod_x*self._unmod_factor

        self.psi = psi_x

    def draw(self, canvas):
        p = normsq(self.psi)*self.dxs.prod()
        canvas.draw_map(p/0.001)
        canvas.draw_map(
            self.V/self.V.max(),
            mask=(self.V != 0),
            color_map='Greys'
        )
