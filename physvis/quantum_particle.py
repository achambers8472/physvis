import numpy as np

from . import space


def normsq(psi):
    return np.abs(psi)**2


class QuantumParticle:
    def __init__(self, x, psi_x, m=1, V=None):
        if V is None:
            V = np.zeros_like(psi_x)

        self.x = x
        self.psi_x = psi_x
        self.m = m
        self.V = V

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self._dxs = self.x[1, 1] - self.x[0, 0]
        x0 = self._x[0, 0]

        Ns = self.x.shape[:-1]

        self._dks = (2*np.pi)/(Ns*self._dxs)
        self._k = space.normal(Ns, self._dks)
        k0 = self._k[0, 0]

        self._k0_dot_x = (k0*self.x).sum(axis=-1)

        self._x_mod_factor = np.exp(-1j*self._k0_dot_x)*self._dxs[0]/(2*np.pi)
        self._x_unmod_factor = np.exp(1j*self._k0_dot_x)*(2*np.pi)/self._dxs[0]

        self._k_unmod_factor = np.exp(-1j*x0*self._k)
        self._k_mod_factor = np.exp(-1j*x0*self._k)

        self._k2 = (self._k**2).sum(axis=-1)

    @property
    def psi_x(self):
        return self._psi_mod_x*self._x_unmod_factor

    @psi_x.setter
    def psi_x(self, psi_x):
        self._psi_mod_x = self._x_mod_factor*psi_x

    @property
    def psi_k(self):
        return self._psi_mod_k*self._k_unmod_factor

    @psi_k.setter
    def psi_k(self, psi_k):
        raise NotImplementedError()
        self._psi_mod_k = self._k_mod_factor*psi_k

    def update(self, dt):
        x_half_up_factor = np.exp((-0.5j*dt)*self.V)

        self._psi_mod_x *= x_half_up_factor

        self._psi_mod_k = np.fft.fft2(self._psi_mod_x)
        self._psi_mod_k *= np.exp((-0.5j*dt/self.m)*self._k2)
        self._psi_mod_x = np.fft.ifft2(self._psi_mod_k)

        self._psi_mod_x *= x_half_up_factor

    def draw(self, canvas):
        p = normsq(self.psi_x)*self._dxs.prod()
        canvas.draw_map(p/0.001)
        canvas.draw_map(
            self.V/self.V.max(),
            mask=(self.V != 0),
            color_map='Greys',
            alpha=0.5,
        )
